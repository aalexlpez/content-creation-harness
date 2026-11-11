#!/usr/bin/env python3
"""Inventario verificable de media antiguos. NUNCA mueve ni elimina archivos.

Ejemplos:
 python scripts/gestion_archivo.py inventariar 2026-W46 V01 --archive-id DISCO_A --relative-path 2026-W46/V01
 python scripts/gestion_archivo.py verificar 2026-W46 V01 --destino X:/Alexander_Archivo/2026-W46/V01
 python scripts/gestion_archivo.py marcar-offline 2026-W46 V01 --confirmo-archivo
"""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'registro' / 'ARCHIVOS.csv'
COLUMNS = ['semana','video_id','storage_status','archive_id', 'archive_relative_path', 'manifest_path', 'last_verified_utc', 'file_count','total_bytes','notes']
MEDIA_DIRS = ['media','preview','delivery','hyperframes','src','assets','capcut','exportaciones','exports','montaje_final','grabaciones_originales']
EXCLUDE = {'node_modules', '.git', '__pycache__', '.cache', '.venv', 'cache'}

def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')

def video_folder(week, video):
    if not re.fullmatch(r'20\d{2}-W\d{2}', week) or not re.fullmatch(r'V\d{2}', video):
        raise ValueError('ID inválido: semana AAAA-WNN y vídeo Vnn')
    folder = ROOT / 'semanas' / week / 'videos' / video
    if not folder.is_dir():
        raise FileNotFoundError(f'No existe el episodio: {folder}')
    return folder

def digest(p):
    d = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            d.update(chunk)
    return d.hexdigest()

def manifest_path(folder):
    return folder / 'ARCHIVO.json'

def load(folder):
    p = manifest_path(folder)
    if not p.exists():
        raise FileNotFoundError('ARCHIVO.json no existe; ejecuta inventariar primero')
    return json.loads(p.read_text(encoding='utf-8'))

def save(folder, manifest):
    manifest_path(folder).write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')

def reg(manifest):
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    previous = []
    if REGISTRY.exists():
        with REGISTRY.open(newline='',encoding='utf-8') as f:
            previous=list(csv.DictReader(f))
    row = dict(semana=manifest['semana'], video_id=manifest['video_id'], storage_status=manifest['storage_status'],
         archive_id=manifest['archive_id'], archive_relative_path=manifest['archive_relative_path'],
         manifest_path=f"semanas/{manifest['semana']}/videos/{manifest['video_id']}/ARCHIVO.json",
         last_verified_utc=manifest.get('last_verified_utc') or '',
         file_count=len(manifest['files']), total_bytes=sum(v['bytes'] for v in manifest['files']),notes='')
    previous=[r for r in previous if (r['semana'],r['video_id']) != (row['semana'],row['video_id'])]
    previous.append(row)
    with REGISTRY.open('w',newline='',encoding='utf-8') as f:
        out=csv.DictWriter(f,fieldnames=COLUMNS)
        out.writeheader()
        out.writerows(previous)

def inventariar(args,folder):
    rel = Path(args.relative_path)
    if rel.is_absolute() or '..' in rel.parts or not args.archive_id.strip():
        raise ValueError('archive-id obligatorio y ruta relativa sin ..')
    if manifest_path(folder).exists():
        raise FileExistsError('Existe ARCHIVO.json. Conservar manifiesto anterior; no sobrescribir automáticamente')
    records=[]
    for d in MEDIA_DIRS:
        base=folder/d
        if not base.is_dir(): continue
        for p in sorted(base.rglob('*')):
            if p.is_symlink():
                raise RuntimeError(f'No se admiten enlaces simbólicos en inventario: {p}')
            if p.is_file() and not any(part in EXCLUDE for part in p.relative_to(folder).parts):
                records.append({'path':p.relative_to(folder).as_posix(), 'bytes':p.stat().st_size, 'sha256':digest(p)})
    if not records:
        raise ValueError('No se encontraron medios en subcarpetas conocidas; revisar el árbol antes de archivar')
    m={'schema_version':1,'semana':args.week,'video_id':args.video,'archive_id':args.archive_id,
        'archive_relative_path':rel.as_posix(),'storage_status':'LOCAL_ACTIVO',
        'inventoried_at_utc':now(),'last_verified_utc':None, 'files':records}
    save(folder,m); reg(m)
    print(f'Inventariados {len(records)} archivos ({sum(x["bytes"] for x in records):,} bytes). NO se movió ni borró nada.')

def verificar(args,folder):
    m=load(folder)
    dest=Path(args.destino)
    if not dest.is_dir():
        raise FileNotFoundError(f'Destino no está montado o no existe: {dest}')
    problems=[]
    for rec in m['files']:
        rel=Path(rec['path'])
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('Ruta insegura en manifiesto')
        p=dest/rel
        if not p.is_file(): problems.append(f'FALTA: {rel}')
        elif p.stat().st_size!=rec['bytes']: problems.append(f'TAMAÑO: {rel}')
        elif digest(p)!=rec['sha256']: problems.append(f'HASH: {rel}')
    if problems:
        print('\n'.join(problems[:40]),file=sys.stderr)
        raise RuntimeError(f'Verificación fallida: {len(problems)} errores. NO limpiar local')
    m['last_verified_utc']=now()
    if m['storage_status']=='LOCAL_ACTIVO':
        m['storage_status']='COPIA_EXTERNA_VERIFICADA'
    save(folder,m); reg(m)
    print(f'Verificada copia externa: {len(m["files"])} archivos, SHA-256 OK. NO se movió ni borró nada.')

def marcar_offline(args,folder):
    m=load(folder)
    if not args.confirmo_archivo:
        raise ValueError('Falta --confirmo-archivo: aprobación expresa')
    if m['storage_status'] not in {'COPIA_EXTERNA_VERIFICADA','ARCHIVADO_OFFLINE'} or not m.get('last_verified_utc'):
        raise ValueError('Primero verificar una copia externa con SHA-256')
    m['storage_status']='ARCHIVADO_OFFLINE'
    save(folder,m); reg(m)
    print('ARCHIVADO_OFFLINE registrado. Los originales LOCALES NO han sido borrados: limpieza es MANUAL.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    a=sub.add_parser('inventariar')
    a.add_argument('week'); a.add_argument('video'); a.add_argument('--archive-id',required=True); a.add_argument('--relative-path',required=True)
    a=sub.add_parser('verificar')
    a.add_argument('week'); a.add_argument('video'); a.add_argument('--destino',required=True)
    a=sub.add_parser('marcar-offline')
    a.add_argument('week'); a.add_argument('video'); a.add_argument('--confirmo-archivo',action='store_true')
    args=parser.parse_args()
    try:
        folder=video_folder(args.week,args.video)
        if args.command=='inventariar': inventariar(args,folder)
        elif args.command=='verificar': verificar(args,folder)
        else: marcar_offline(args,folder)
    except (FileNotFoundError,ValueError,RuntimeError,FileExistsError) as e:
        print('ERROR:',e,file=sys.stderr)
        sys.exit(1)

if __name__=='__main__':main()
