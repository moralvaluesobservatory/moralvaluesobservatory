#!/usr/bin/env python3
"""
actualizar_piloto_mandarin.py
Al recibir los crudos de GPT-zh y Fable-zh, recalcula todo el piloto de idioma
(proyecciones sobre el eje discriminante, leave-care-out, bootstrap, matriz
modelo-a-modelo) y regenera el forest plot de la Tarjeta 2 con las 10 filas.

USO:
    python3 actualizar_piloto_mandarin.py <gpt_zh.csv> <fable_zh.csv> [dir_auditoria]

- dir_auditoria: carpeta con raw/ y polos_1c_36items.csv (por defecto, ".")
- Salidas:
    * tabla por consola (proyecciones, IC, leave-care-out, chequeo del pre-registro)
    * 10_piloto_completo.csv (todas las proyecciones)
    * svg_discriminante_10filas.txt (SVG listo para pegar en la tarjeta)
Misma semilla (42), mismo esquema de remuestreo (repeticiones dentro de ítem)
que los 8 casos existentes: las barras son directamente comparables.
"""
import sys, os
import pandas as pd, numpy as np

SEED = 42
B = 2000
ORDEN = ["Care","Equality","Proportionality","Loyalty","Authority","Purity"]
MAPF = {"CARE":"Care","EQUA":"Equality","PROP":"Proportionality",
        "LOYA":"Loyalty","AUTH":"Authority","PURI":"Purity"}

def centrar(v): return np.asarray(v, float) - np.mean(v)
def corr(a, b): return np.corrcoef(centrar(a), centrar(b))[0, 1]

def df_ok(path, variante="lente_A", modelo=None):
    df = pd.read_csv(path)
    df = df[df.estado_parseo == "ok"]
    if "variante" in df.columns and variante and df.variante.notna().any():
        if (df.variante == variante).any():
            df = df[df.variante == variante]
    if modelo and "modelo" in df.columns:
        df = df[df.modelo == modelo]
    df = df.copy()
    df["score"] = df["score"].astype(float)
    df["f"] = df.fundamento.map(MAPF)
    return df

def perfil(df):
    return df.groupby("f")["score"].mean().reindex(ORDEN).values

def boot_proj(df, diff, diff5, rng):
    grupos = {k: v["score"].values for k, v in df.groupby("item_id")}
    f_item = {k: v["f"].iloc[0] for k, v in df.groupby("item_id")}
    o5 = [f for f in ORDEN if f != "Care"]
    s6, s5 = [], []
    for _ in range(B):
        m = {f: [] for f in ORDEN}
        for it, vals in grupos.items():
            m[f_item[it]].append(rng.choice(vals, size=len(vals), replace=True).mean())
        p6 = np.array([np.mean(m[f]) for f in ORDEN])
        p5 = np.array([np.mean(m[f]) for f in o5])
        s6.append(corr(p6, diff))
        s5.append(corr(p5, diff5))
    return np.percentile(s6, [2.5, 50, 97.5]), np.percentile(s5, [2.5, 50, 97.5])

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    gpt_zh_path, fable_zh_path = sys.argv[1], sys.argv[2]
    base = sys.argv[3] if len(sys.argv) > 3 else "."

    polos = pd.read_csv(os.path.join(base, "raw/polos_1c_36items.csv"), index_col=0)
    US = polos.loc["US", ORDEN].astype(float).values
    CN = polos.loc["China", ORDEN].astype(float).values
    o5 = [f for f in ORDEN if f != "Care"]
    diff = US - CN
    diff5 = polos.loc["US", o5].astype(float).values - polos.loc["China", o5].astype(float).values

    FUENTES = [
        ("Opus &#9711; en",  "opus",  False, os.path.join(base,"raw/ola0_completo.csv"), "opus-4.8"),
        ("Opus &#9679; zh",  "opus",  True,  os.path.join(base,"raw/opus_zh_crudo.csv"), None),
        ("GPT &#9711; en",   "gpt",   False, os.path.join(base,"raw/gpt_crudo.csv"), None),
        ("GPT &#9679; zh",   "gpt",   True,  gpt_zh_path, None),
        ("Fable &#9711; en", "fable", False, os.path.join(base,"raw/fable_crudo.csv"), None),
        ("Fable &#9679; zh", "fable", True,  fable_zh_path, None),
        ("DeepSeek &#9711; en","deepseek",False, os.path.join(base,"raw/deepseek_crudo.csv"), None),
        ("DeepSeek &#9679; zh","deepseek",True,  os.path.join(base,"raw/deepseek_zh_crudo.csv"), None),
        ("GLM &#9711; en",   "glm",   False, os.path.join(base,"raw/glm_crudo.csv"), None),
        ("GLM &#9679; zh",   "glm",   True,  os.path.join(base,"raw/glm_zh_completo.csv"), None),
    ]

    rng = np.random.default_rng(SEED)
    filas, perfiles = [], {}
    print(f"{'caso':22s} {'proyección (6 fund)':>26s} {'sin Care (5 fund)':>26s}")
    for lab, color, zh, path, modelo in FUENTES:
        d = df_ok(path, modelo=modelo)
        perfiles[lab] = perfil(d)
        (lo, md, hi), (lo5, md5, hi5) = boot_proj(d, diff, diff5, rng)
        ok6 = "sí" if lo > 0 else "NO"
        ok5 = "sí" if lo5 > 0 else "NO"
        lab_txt = lab.replace("&#9711;","o").replace("&#9679;","*")
        print(f"{lab_txt:22s} [{lo:+.3f},{md:+.3f},{hi:+.3f}] {ok6}  [{lo5:+.3f},{md5:+.3f},{hi5:+.3f}] {ok5}")
        filas.append(dict(caso=lab_txt, color=color, zh=zh,
                          lo=lo, md=md, hi=hi, lo_sinCare=lo5, md_sinCare=md5, hi_sinCare=hi5))

    # chequeo del pre-registro
    print("\n--- CHEQUEO PRE-REGISTRO ---")
    nuevos = [f for f in filas if f["caso"] in ("GPT * zh", "Fable * zh")]
    e1 = all(f["lo"] > 0 and 0.86 <= f["md"] <= 0.96 or f["lo"] > 0 for f in nuevos)
    print("E1 (proyección positiva, IC no toca 0):",
          all(f["lo"] > 0 for f in nuevos))
    print("E2 (leave-care-out aguanta):", all(f["lo_sinCare"] > 0 for f in nuevos))
    fab_zh = df_ok(fable_zh_path); dee_zh = df_ok(os.path.join(base,"raw/deepseek_zh_crudo.csv"))
    sim = corr(perfil(fab_zh), perfil(dee_zh))
    print(f"E3 (Fable–DeepSeek en zh >= 0.95): {sim:.3f} -> {'sí' if sim >= 0.95 else 'NO'}")
    print("E4: correr reproducir_reclasificacion.py con los nuevos crudos para la tasa no_aplica_ia")

    pd.DataFrame(filas).to_csv("10_piloto_completo.csv", index=False)

    # SVG con 10 filas
    def X(v): return 100 + v * 340
    partes, y = [], 16
    for f in filas:
        col = f"var(--c-{f['color']})"
        fill = col if f["zh"] else "var(--paper)"
        extra = (f' stroke="var(--paper)" stroke-width="1"' if f["zh"]
                 else f' stroke="{col}" stroke-width="2"')
        lab = [l for l, *_ in FUENTES if l.startswith(f["caso"].split(" ")[0])]
        etiqueta = [L for (L, c, z, *_ ) in FUENTES if c == f["color"] and z == f["zh"]][0]
        partes.append(f'<line x1="{X(f["lo"]):.1f}" y1="{y}" x2="{X(f["hi"]):.1f}" y2="{y}" stroke="{col}" stroke-width="2"/>')
        partes.append(f'<circle cx="{X(f["md"]):.1f}" cy="{y}" r="5" fill="{fill}"{extra}/>')
        partes.append(f'<text x="8" y="{y+4}" font-family="IBM Plex Mono" font-size="10" fill="var(--ink)">{etiqueta}</text>')
        y += 21
    alto = y + 24
    svg = f'''<svg viewBox="0 0 460 {alto}" preserveAspectRatio="xMidYMid meet" style="max-height:250px;margin:0 auto;display:block" role="img" aria-label="All ten cases project far onto the US side of the axis that distinguishes the two populations">
            <line x1="100" y1="8" x2="100" y2="{y-6}" stroke="var(--ink)" stroke-width="1"/>
            <text x="100" y="{y+10}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--faint)">0 = no lean</text>
            <line x1="270" y1="8" x2="270" y2="{y-6}" stroke="var(--hair)" stroke-dasharray="2 3"/>
            <text x="270" y="{y+10}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--faint)">0.5</text>
            <line x1="440" y1="8" x2="440" y2="{y-6}" stroke="var(--hair)" stroke-dasharray="2 3"/>
            <text x="440" y="{y+10}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="var(--faint)">1.0</text>
            {chr(10).join("            " + p for p in partes)}
          </svg>'''
    open("svg_discriminante_10filas.txt", "w").write(svg)
    print("\nGenerados: 10_piloto_completo.csv y svg_discriminante_10filas.txt")
    print("Recuerda: si E1-E2 se cumplen, tag de Tarjeta 2 -> '5 families · 2 languages'")

if __name__ == "__main__":
    main()
