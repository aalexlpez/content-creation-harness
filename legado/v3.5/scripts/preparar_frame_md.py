"""Genera frame.md SOLO desde identidad aprobada; no concede la aprobación."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
src = root / 'brand' / 'IDENTIDAD_APROBADA.json'
if not src.exists():
    raise SystemExit('BLOQUEADO B0: falta brand/IDENTIDAD_APROBADA.json')
x = json.loads(src.read_text(encoding='utf-8'))
if x.get('status') != 'APROBADA' or not x.get('approved_by') or not x.get('approved_at'):
    raise SystemExit('BLOQUEADO: status APROBADA, approved_by y approved_at obligatorios')
c = x['colors']
required = ['background', 'surface', 'text_primary', 'text_secondary', 'accent_primary', 'accent_secondary', 'accent_result']
if any(not c.get(k) for k in required):
    raise SystemExit('BLOQUEADO: faltan tokens')
lines = [
    '# frame.md — Alexander / identidad AUDIOVISUAL PERSONAL (MiMiniApp es producto)' ,
    '',
    f"Aprobada por {x['approved_by']} el {x['approved_at']}. Versión: {x.get('version', 'sin-versión')}.",
    '',
    '## Color tokens aprobados',
]
lines += [f'- {k}: `{c[k]}`' for k in required]
lines += [
    '', '## Principios de composición',
    '- Identidad del creador: Alexander (no MiMiniApp). No inventar handle; registrar solo si fue comprobado y aprobado.',
    '- Video 9:16. Una idea protagonista por plano.',
    '- Rostro del creador para confianza; transiciones UI para explicar.',
    '- Morph visual, rótulos breves y efectos sonoros con intención.',
    '- Los colores no se heredan de la web. No copiar referencias ajenas.',
    '', '## Canon',
    '- Tokens procedentes de identidad aprobada y versionada.',
    '- Cada vídeo añade guion, storyboard y claims validados propios.',
]
p = root / 'frame.md'
if p.exists():
    raise SystemExit('Ya existe frame.md, revisar antes de sobrescribir')
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Creado', p)
