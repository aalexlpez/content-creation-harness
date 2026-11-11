#!/usr/bin/env python3
"""Inspecciona original/master usando ffprobe. NO modifica archivo ni sustituye QC humano."""
import argparse, json, subprocess, sys
from pathlib import Path
from fractions import Fraction
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('video',type=Path)
p.add_argument('--master',action='store_true',help='Validar presencia de vídeo/audio, 1080x1920, h264 y FPS esperado')
p.add_argument('--fps',type=float,default=30.0)
a=p.parse_args()
if not a.video.is_file(): raise SystemExit(f'No existe: {a.video}')
try:
    r=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,pix_fmt,color_space,color_transfer,color_primaries,sample_rate,channels,bit_rate','-of','json',str(a.video)],capture_output=True,text=True,check=True)
except FileNotFoundError: raise SystemExit('ffprobe no instalado; instalar FFmpeg o registrar metadatos manualmente')
except subprocess.CalledProcessError as e: raise SystemExit(f'ffprobe ERROR: {e.stderr}')
x=json.loads(r.stdout); stream=x.get('streams',[]);vs=next((v for v in stream if v.get('codec_type')=='video'),None)
as_=next((v for v in stream if v.get('codec_type')=='audio'),None)
if not vs:raise SystemExit('No hay pista de vídeo')
try:fps=float(Fraction(vs.get('avg_frame_rate','0')))
except Exception:fps=0
result={'file':str(a.video),'video':{'codec':vs.get('codec_name'),'width':vs.get('width'),'height':vs.get('height'),'fps_avg':round(fps,3),'fps_nominal':vs.get('r_frame_rate'),'pixel_format':vs.get('pix_fmt'),'color_primaries':vs.get('color_primaries'),'color_transfer':vs.get('color_transfer'),'color_space':vs.get('color_space'),'bitrate':vs.get('bit_rate')},'audio':({'codec':as_.get('codec_name'),'sample_rate':as_.get('sample_rate'),'channels':as_.get('channels')} if as_ else None),'format':x.get('format',{})}
errors=[];warnings=[]
if a.master:
    if (vs.get('width'),vs.get('height'))!=(1080,1920):errors.append('Resolución distinta a 1080x1920')
    if abs(fps-a.fps)>0.15:errors.append(f'FPS {fps:.3f} distinto del plan {a.fps}')
    if vs.get('codec_name')!='h264':errors.append('Códec distinto a h264')
    if not as_:errors.append('Master sin audio (bloquea si guion exige voz/sonido)')
    elif as_.get('codec_name')!='aac':warnings.append('Audio distinto a AAC: verificar destino')
    elif as_.get('sample_rate')!='48000':warnings.append('Audio distinto a 48 kHz')
    if not vs.get('color_primaries') or vs.get('color_primaries') in ['unknown','unspecified']:
        warnings.append('Color sin primarias especificadas, verificar Rec.709/HDR')
    elif vs.get('color_primaries')!='bt709':warnings.append('Color diferente BT.709: comprobar política de HDR/SDR')
result['master_check']={'errors':errors,'warnings':warnings,'pass_metadata':len(errors)==0}
print(json.dumps(result,indent=2,ensure_ascii=False))
if errors:sys.exit(2)
