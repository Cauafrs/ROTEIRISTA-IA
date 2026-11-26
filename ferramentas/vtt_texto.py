# -*- coding: utf-8 -*-
"""Converte as legendas automáticas (.vtt) do YouTube em roteiro limpo: tira as linhas repetidas
da legenda "rolante" e marca o tempo a cada ~15 s. Também mede palavras por minuto.
Uso: python vtt_texto.py <pasta_legendas>/  -> grava roteiros/<id>.txt e roteiros/_metricas.tsv"""
import re, sys, glob, os

pasta = sys.argv[1] if len(sys.argv) > 1 else "legendas"
out = os.path.join(os.path.dirname(os.path.abspath(pasta.rstrip("/"))), "roteiros")
os.makedirs(out, exist_ok=True)
titulos = {}
lista = os.path.join(os.path.dirname(out), "canal_completo.txt")   # opcional: id|título|views|duração
if os.path.exists(lista):
    for l in open(lista, encoding="utf-8", errors="ignore"):
        p = l.strip().split("|")
        if len(p) >= 4:
            titulos[p[0]] = (p[1], p[2], p[3])


def seg(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


met = []
arqs = {}
for f in glob.glob(os.path.join(pasta, "*.vtt")):
    vid = os.path.basename(f).split(".")[0]
    # prefere a legenda original em português (pt-orig > pt)
    pri = 0 if ".pt-orig." in f else (1 if ".pt." in f else 2)
    if vid not in arqs or pri < arqs[vid][0]:
        arqs[vid] = (pri, f)

for vid, (_, f) in arqs.items():
    txt = open(f, encoding="utf-8", errors="ignore").read()
    blocos = re.split(r"\n\n+", txt)
    linhas, vistos = [], []
    for b in blocos:
        m = re.search(r"(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)", b)
        if not m:
            continue
        t0 = seg(m.group(1))
        corpo = [re.sub(r"<[^>]+>", "", x).strip() for x in b.split("\n")[1:]]
        for c in corpo:
            if not c or c in vistos[-3:]:
                continue
            vistos.append(c)
            linhas.append((t0, c))
    # junta em texto com marca de tempo a cada 15 s
    res, ult = [], -99
    for (t, c) in linhas:
        if t - ult >= 15:
            res.append(f"\n[{int(t // 60):02d}:{int(t % 60):02d}] ")
            ult = t
        res.append(c + " ")
    texto = "".join(res).strip()
    n = len(re.findall(r"\w+", texto))
    dur = linhas[-1][0] if linhas else 1
    tit, views, d = titulos.get(vid, ("?", "?", "?"))
    met.append((vid, tit, views, d, n, round(n / max(1, dur / 60))))
    open(os.path.join(out, vid + ".txt"), "w", encoding="utf-8").write(f"# {tit} ({vid}) — {views} mil views, {d}s\n{texto}\n")

with open(os.path.join(out, "_metricas.tsv"), "w", encoding="utf-8") as fo:
    fo.write("id\ttitulo\tmil_views\tdur_s\tpalavras\tpal_por_min\n")
    for m in sorted(met, key=lambda x: -int(x[2]) if str(x[2]).isdigit() else 0):
        fo.write("\t".join(str(x) for x in m) + "\n")
print(len(met), "roteiros em", out)
