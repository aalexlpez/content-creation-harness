#!/usr/bin/env python3
"""Comprueba archivos críticos, manifest SHA-256 y unicidad de IDs de prompts."""
from pathlib import Path
from hashlib import sha256
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
required=['00_INICIO_Y_ESTADO.md','01_EVIDENCIA_Y_AUDITORIA.md','02_ESTRATEGIA_EDITORIAL.md',
 '03_IDENTIDAD_AUDIOVISUAL.md','04_SISTEMA_DE_GUIONES.md','05_SOP_SEMANAL_Y_GATES.md',
 '06_OPERACION_COWORK_CLAUDECODE.md','07_ESPECIFICACION_HYPERFRAMES.md','08_MEDICION_Y_APRENDIZAJE.md',
 '09_PROMPTS_MAESTROS.md','12_IDENTIDAD_PERSONAL_Y_HANDLES.md','13_GUIA_OPERATIVA_COWORK_WORK_CHATGPT_WEB.md',
 '14_POLITICA_ARCHIVO_Y_RESTAURACION.md','15_MONTAJE_FINAL_GRATUITO.md',
 '16_GUIA_SEMANA_EN_15_MINUTOS.md','17_AUDITORIA_FINAL_ESTANDARES.md',
 '18_INGESTA_COLOR_EXPORT_Y_QC.md','19_MAPA_DOCUMENTAL_Y_FRECUENCIA.md','CLAUDE.md','COWORK_INSTRUCCIONES.md',
 'registro/DECISIONES.md','registro/ESTADO.md','registro/ARCHIVOS.csv','brand/IDENTIDAD_PROPUESTA.json',
 'scripts/crear_semana.py','scripts/gestion_archivo.py','scripts/inspeccionar_video.py']
errors=[]
for name in required:
 if not (ROOT/name).is_file():errors.append('FALTA '+name)
photos=sorted((ROOT/'referencias/ui_motion').glob('*.jpg'))
if sorted(p.name for p in photos)!=['1000845575.jpg','1000845576.jpg','1000845577.jpg']:
 errors.append('FALTAN 3 JPG ORIGINALES')
text=(ROOT/'09_PROMPTS_MAESTROS.md').read_text(encoding='utf-8')
ids=re.findall(r'^## (P\d{2}) —',text,flags=re.MULTILINE)
if len(ids)!=len(set(ids)) or ids!=[f'P{i:02d}' for i in range(19)]:
 errors.append(f'PROMPTS IDs incorrectos o duplicados: {ids}')
p=ROOT/'MANIFEST_SHA256.json'
if not p.is_file():errors.append('FALTA MANIFEST_SHA256.json')
else:
 m=json.loads(p.read_text(encoding='utf-8'))
 if m.get('version')!='3.5':errors.append('MANIFEST versión no coincide')
 for name,digest in m.get('files',{}).items():
  f=ROOT/name
  if not f.is_file():errors.append('NO EXISTE en manifest '+name)
  elif sha256(f.read_bytes()).hexdigest()!=digest:errors.append('HASH DIFERENTE '+name)
print('Archivos críticos:',len(required)-len([e for e in errors if e.startswith('FALTA ') ]),'/',len(required))
print('Fotos originales:',len(photos),'/3; prompts IDs:',len(ids),'/19')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('VALIDACIÓN COMPLETA OK (integridad y estructura; no prueba rendimiento visual)')
