#!/usr/bin/env python3
"""Crea semana documental y expedientes en BORRADOR. No aprueba ni publica nada."""
import shutil, re, sys
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)!=3 or not re.fullmatch(r'20\d{2}-W(?:0[1-9]|[1-4]\d|5[0-3])',sys.argv[1]) or not sys.argv[2].isdigit():
    raise SystemExit('Uso: python scripts/crear_semana.py 2026-W46 2   [0..6]')
week,n=sys.argv[1],int(sys.argv[2]);
if not (0<=n<=6): raise SystemExit('Número de expedientes 0..6')
folder=ROOT/'semanas'/week
if folder.exists(): raise SystemExit('La semana ya existe; se bloquea sobreescritura')
folder.mkdir(parents=True)
shutil.copy2(ROOT/'templates/SEMANA.md',folder/'PLAN.md')
shutil.copy2(ROOT/'templates/CIERRE_SEMANAL.md',folder/'RETRO.md')
(folder/'ideas').mkdir(exist_ok=True)
for i in range(1,n+1):
    d=folder/'videos'/f'V{i:02d}'; d.mkdir(parents=True)
    for name,dest in [
        ('VIDEO.md','BRIEF.md'),('SCRIPT.md','SCRIPT.md'),
        ('PRUEBAS_Y_CLAIMS.md','PRUEBAS_Y_CLAIMS.md'),('TAKES.md','TAKES.md'),
        ('INGESTA.md','INGESTA.md'),('EDIT_PLAN.md','EDIT_PLAN.md'),
        ('REVISION.md','REVISION.md'),('MONTAJE_FINAL.md','MONTAJE_FINAL.md'),
        ('LICENCIAS_MEDIOS.md','LICENCIAS_MEDIOS.md'),('QC_MASTER.md','QC_MASTER.md'),
        ('PUBLICACION.md','PUBLICACION.md')]:
        shutil.copy2(ROOT/'templates'/name,d/dest)
    for sub in ['media/camera/original','media/camera/proxy','media/audio','media/referencias',
                'media/datos_verificados','hyperframes','src','exports/escenas','exports/audio',
                'exports/captions','exports/grafismos','preview','montaje_final','delivery']:
        (d/sub).mkdir(parents=True,exist_ok=True)
print('CREADA',folder,'con',n,'expedientes BORRADOR, sin aprobaciones ni trabajos automáticos')
