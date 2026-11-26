# -*- coding: utf-8 -*-
"""Mede a edição dos vídeos baixados: cortes (detecção de cena do ffmpeg), cortes por minuto no geral,
no 1º minuto e no resto, duração mediana do plano; e monta folhas de quadros (1 quadro/s) do 1º minuto
e de um minuto do meio. Uso: python edicao_metricas.py videos/"""
import os, sys, glob, re, subprocess, statistics
from PIL import Image, ImageDraw

FF = os.path.expanduser("~/.claude/skills/video-analyze/bin/ffmpeg.exe")
FP = os.path.expanduser("~/.claude/skills/video-analyze/bin/ffprobe.exe")
pasta = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(pasta.rstrip("/"))), "edicao")
os.makedirs(OUT, exist_ok=True)


def dur(f):
    return float(subprocess.run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout.strip())


def cortes(f, th=0.28):
    r = subprocess.run([FF, "-hide_banner", "-i", f, "-vf", f"scale=320:-2,select='gt(scene,{th})',showinfo", "-an", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="ignore").stderr
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", r)]


def folha(f, t0, n, nome, cols=10):
    w, h = 192, 108
    g = Image.new("RGB", (cols * w, ((n + cols - 1) // cols) * (h + 14)), (0, 0, 0))
    d = ImageDraw.Draw(g)
    p = subprocess.run([FF, "-v", "error", "-ss", str(t0), "-i", f, "-t", str(n), "-vf", f"fps=1,scale={w}:{h}",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    k = 0
    for k in range(min(n, len(p) // (w * h * 3))):
        im = Image.frombuffer("RGB", (w, h), p[k * w * h * 3:(k + 1) * w * h * 3], "raw", "RGB", 0, 1)
        x, y = (k % cols) * w, (k // cols) * (h + 14)
        g.paste(im, (x, y + 14))
        s = int(t0 + k)
        d.text((x + 3, y), f"{s // 60}:{s % 60:02d}", fill=(255, 255, 0))
    g.save(os.path.join(OUT, nome), quality=80)


linhas = ["id\tdur_s\tcortes\tcortes_min\tcortes_min_1o_min\tplano_mediano_s"]
for f in sorted(glob.glob(os.path.join(pasta, "*.mp4"))):
    vid = os.path.basename(f)[:-4]
    D = dur(f)
    c = cortes(f)
    planos = [b - a for a, b in zip([0] + c, c + [D])]
    c1 = len([x for x in c if x < 60])
    linhas.append(f"{vid}\t{D:.0f}\t{len(c)}\t{len(c) / (D / 60):.1f}\t{c1}\t{statistics.median(planos):.2f}")
    open(os.path.join(OUT, vid + "_cortes.txt"), "w").write("\n".join(f"{x:.2f}" for x in c))
    folha(f, 0, 60, vid + "_min1.jpg")
    folha(f, int(D / 2), 60, vid + "_meio.jpg")
    print(linhas[-1], flush=True)
open(os.path.join(OUT, "_metricas_edicao.tsv"), "w").write("\n".join(linhas) + "\n")
