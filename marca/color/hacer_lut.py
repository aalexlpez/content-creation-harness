"""LUT .cube «cine cálido» para tomas Rec.709 de celular (POCO F5). Solo biblioteca estándar.
Uso: python marca/color/hacer_lut.py marca/color/cine_calido_v02.cube
Pasos por color: curva en S con negros levemente levantados (mate), sombras hacia azul verdoso y luces hacia
cálido, protección de piel (tonos naranjas conservan saturación y ganan calidez), resto algo menos saturado.
"""
import colorsys, math, sys

N = 33


def curva(x):
    x = min(1.0, max(0.0, x))
    x = 1 - (1 - x) ** 1.25                  # exposición: levanta medios sin quemar luces (tomas de celular oscuras)
    s = x * x * (3 - 2 * x)                 # S suave
    y = 0.72 * x + 0.28 * s                 # mezcla: contraste moderado
    return 0.035 + y * (0.975 - 0.035)       # negros mate, blancos sin quemar


def lut(r, g, b):
    r, g, b = curva(r), curva(g), curva(b)
    l = 0.2126 * r + 0.7152 * g + 0.0722 * b
    som = (1 - l) ** 2                       # peso de sombras
    luz = l ** 2                             # peso de luces
    r += -0.018 * som + 0.050 * luz + 0.010
    g += 0.006 * som + 0.012 * luz
    b += 0.028 * som - 0.045 * luz - 0.008
    r, g, b = [min(1, max(0, v)) for v in (r, g, b)]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    deg = h * 360
    piel = math.exp(-(((deg - 25 + 180) % 360 - 180) / 22) ** 2)   # piel ≈ 25°
    s *= 0.90 + 0.22 * piel                  # resto −10 %, piel +12 %
    if piel > 0.01:                          # piel: un poco más cálida y luminosa
        h = (h - 0.004 * piel) % 1.0
        v = min(1.0, v * (1 + 0.07 * piel))
    return colorsys.hsv_to_rgb(h, s, v)


def main(path):
    with open(path, "w", encoding="ascii") as f:
        f.write('TITLE "cerobytes cine calido v02"\n')
        f.write(f"LUT_3D_SIZE {N}\nDOMAIN_MIN 0 0 0\nDOMAIN_MAX 1 1 1\n")
        for bi in range(N):              # el orden .cube: R varía más rápido
            for gi in range(N):
                for ri in range(N):
                    r, g, b = lut(ri / (N - 1), gi / (N - 1), bi / (N - 1))
                    f.write(f"{r:.6f} {g:.6f} {b:.6f}\n")


if __name__ == "__main__":
    main(sys.argv[1])
