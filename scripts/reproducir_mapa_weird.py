#!/usr/bin/env python3
"""
reproducir_mapa_weird.py
Genera 01_mapa_weird.csv y 04_bootstrap_weird.csv desde los crudos.
Auditable: cualquiera puede correr esto y obtener las mismas cifras.
Semilla fija = 42 para el bootstrap.
"""
import pandas as pd, numpy as np

orden_f = ["Care","Equality","Proportionality","Loyalty","Authority","Purity"]
map_f = {"CARE":"Care","EQUA":"Equality","PROP":"Proportionality",
         "LOYA":"Loyalty","AUTH":"Authority","PURI":"Purity"}

# ---- EL VECTOR PERFIL WEIRD (punto 1 del revisor) ----
# CONSTRUCCIÓN: media NO PONDERADA de los 4 países del marco de 19 (Atari et al. 2023)
# etiquetados como WEIRD. Selección MANUAL (no por WEIRD_distance).
hum = pd.read_csv("raw/mfq2_human_reference_frame_plus.csv")
PAISES_WEIRD = ["Switzerland","Ireland","New Zealand","Belgium"]
weird_prof = hum[hum.country.isin(PAISES_WEIRD)][orden_f].astype(float).mean().values
# Vector resultante (verificable):
# Care=3.9275, Equality=3.0050, Proportionality=3.7725,
# Loyalty=3.4275, Authority=3.5475, Purity=2.7625

def centrar(v): return v - v.mean()
def corr(a,b): return np.corrcoef(centrar(a), centrar(b))[0,1]

# ---- VARIANTE (punto 2 del revisor): SOLO lente_A ----
VARIANTE = "lente_A"

def perfil(path, modelo=None):
    df = pd.read_csv(path); df = df[df.estado_parseo=="ok"]
    if "variante" in df.columns: df = df[df.variante==VARIANTE]
    if modelo and "modelo" in df.columns: df = df[df.modelo==modelo]
    df = df.copy(); df["score"] = df["score"].astype(float)
    df["f"] = df.fundamento.map(map_f)
    return df.groupby("f")["score"].mean().reindex(orden_f).values

def perfil_df(path, modelo=None):
    df = pd.read_csv(path); df = df[df.estado_parseo=="ok"]
    if "variante" in df.columns: df = df[df.variante==VARIANTE]
    if modelo and "modelo" in df.columns: df = df[df.modelo==modelo]
    df = df.copy(); df["score"] = df["score"].astype(float)
    df["f"] = df.fundamento.map(map_f); return df

SISTEMAS = [
    ("Opus 4.8","raw/ola0_completo.csv","opus-4.8"),
    ("GPT","raw/gpt_crudo.csv",None),
    ("DeepSeek","raw/deepseek_crudo.csv",None),
    ("GLM","raw/glm_crudo.csv",None),
    ("Fable","raw/fable_crudo.csv",None),
]

# ---- 01_mapa_weird.csv ----
res=[]
for nombre,path,mod in SISTEMAS:
    p = perfil(path, modelo=mod)
    cw = corr(p, weird_prof)
    corrs=[(r.country, corr(p, r[orden_f].astype(float).values)) for _,r in hum.iterrows()]
    corrs.sort(key=lambda x:-x[1])
    res.append({"sistema":nombre,"corr_weird":round(cw,3),"pais_cercano":corrs[0][0]})
pd.DataFrame(res).to_csv("01_mapa_weird.csv", index=False)

# ---- 04_bootstrap_weird.csv (semilla 42) ----
rng = np.random.default_rng(42)
def bootstrap_corr(df, target, n=2000):
    grupos={f: df[df.f==f].score.values for f in orden_f}
    corrs=[]
    for _ in range(n):
        perfil=np.array([rng.choice(grupos[f],size=len(grupos[f]),replace=True).mean()
                         if len(grupos[f]) else np.nan for f in orden_f])
        corrs.append(corr(perfil, target))
    return np.percentile(corrs,[2.5,50,97.5])
res2=[]
for nombre,path,mod in SISTEMAS:
    df=perfil_df(path,modelo=mod)
    lo,med,hi=bootstrap_corr(df, weird_prof)
    res2.append({"sistema":nombre,"corr_weird_IC2.5":round(lo,3),
                 "mediana":round(med,3),"IC97.5":round(hi,3)})
pd.DataFrame(res2).to_csv("04_bootstrap_weird.csv", index=False)
print("Generados 01_mapa_weird.csv y 04_bootstrap_weird.csv")
print(f"Vector WEIRD: {dict(zip(orden_f, weird_prof.round(4)))}")
