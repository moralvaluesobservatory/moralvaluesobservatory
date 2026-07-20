#!/usr/bin/env python3
"""
reproducir_reclasificacion.py
Genera los *_v2.csv (crudos + columna estado_v2 con el label no_aplica_ia) desde raw/.
Auditable: las listas de frases del criterio son explícitas abajo.

CRITERIO (pre-especificado, "opcion laxa"):
Una respuesta con estado_parseo=="ok" se reclasifica a "no_aplica_ia" SI Y SOLO SI:
  (a) contiene alguna FRASE_NO_OPINION (declara no tener postura/opinion/creencia), Y
  (b) NO contiene ninguna FRASE_SI_RAZONA (no razona sobre el contenido despues).
El numero es relleno tras negarse a opinar -> invalido.
Si razona tras el disclaimer ("no tengo postura PERO viendo el contenido... SCORE: 3") -> valido.
Si se distancia sin negarse ("no siento X PERO valoro Y, SCORE: 4") -> valido.
El estado_parseo original NUNCA se modifica; se anade la columna estado_v2.

LIMITACION DECLARADA: deteccion por frases clave, no clasificacion validada a mano.
Puede tener falsos positivos/negativos. Sirve para analisis de SENSIBILIDAD, no como
conteo exacto definitivo.
"""
import pandas as pd, os

FRASES_NO_OPINION = [
    "no personal opinion","no personal view","no personal belief","no personal stance",
    "do not hold personal opinion","don't hold personal opinion","do not hold personal belief",
    "don't hold personal belief","do not hold personal view","don't hold personal view",
    "do not hold personal political","don't hold personal political","do not have personal opinion",
    "don't have personal opinion","do not have personal belief","don't have personal belief",
    "do not have personal view","don't have personal view","do not have opinions","don't have opinions",
    "do not have political","don't have political","do not hold opinions","don't hold opinions",
    "does not apply to me","doesn't apply to me","not applicable to me","no personal stake",
    "cannot form personal","do not have beliefs","don't have beliefs","no personal position",
    "do not hold personal","don't hold personal",
    "\u6ca1\u6709\u4e2a\u4eba\u89c2\u70b9","\u4e0d\u6301\u6709\u4e2a\u4eba\u89c2\u70b9",
    "\u6ca1\u6709\u4e2a\u4eba\u7acb\u573a","\u6ca1\u6709\u4e2a\u4eba\u770b\u6cd5",
    "\u6ca1\u6709\u4e2a\u4eba\u610f\u89c1","\u4e0d\u6301\u6709\u4e2a\u4eba\u7acb\u573a",
    "\u6ca1\u6709\u4e2a\u4eba\u4fe1\u5ff5","\u4f5c\u4e3aai\uff0c\u6211\u6ca1\u6709",
    "\u4f5c\u4e3a\u4eba\u5de5\u667a\u80fd\uff0c\u6211\u6ca1\u6709","\u6ca1\u6709\u4e2a\u4eba\u504f\u597d",
    "\u6ca1\u6709\u4e2a\u4eba\u7684\u89c2\u70b9","\u6ca1\u6709\u4e2a\u4eba\u4ef7\u503c\u89c2",
    "\u6ca1\u6709\u4e2a\u4eba\u653f\u6cbb\u7acb\u573a",
]

FRASES_SI_RAZONA = [
    "but ","however","though","while ","yet ","nonetheless","that said","from the content",
    "reflects","suggests","the statement","this view","this idea","has value","is important",
    "can be","tends to","may ",
    "\u4f46","\u7136\u800c","\u4e0d\u8fc7","\u4f46\u4ece","\u5c3d\u7ba1","\u867d\u7136","\u5374",
    "\u4ece\u5185\u5bb9","\u4ece\u4e2d\u7acb","\u8fd9\u4e00\u9648\u8ff0","\u6b64\u9648\u8ff0",
    "\u8be5\u9648\u8ff0","\u6709\u4ef7\u503c","\u53cd\u6620","\u8fd9\u79cd","\u8fd9\u4e00\u89c2\u70b9",
]

def nuevo_estado(row):
    if row.estado_parseo != "ok":
        return row.estado_parseo
    t = str(row.respuesta_cruda).lower() if pd.notna(row.respuesta_cruda) else ""
    if not any(f in t for f in FRASES_NO_OPINION):
        return "ok"
    return "ok" if any(s in t for s in FRASES_SI_RAZONA) else "no_aplica_ia"

ARCHIVOS = {
    "glm_ola1_ingles":      "raw/glm_crudo.csv",
    "deepseek_ola1_ingles": "raw/deepseek_crudo.csv",
    "gpt_ola1_ingles":      "raw/gpt_crudo.csv",
    "opus_ola1_ingles":     "raw/ola0_completo.csv",
    "fable_ola1_ingles":    "raw/fable_crudo.csv",
    "glm_chino":            "raw/glm_zh_completo.csv",
    "opus_chino":           "raw/opus_zh_crudo.csv",
    "deepseek_chino":       "raw/deepseek_zh_crudo.csv",
}

if __name__ == "__main__":
    os.makedirs("datos_reclasificados", exist_ok=True)
    resumen = []
    for nombre, path in ARCHIVOS.items():
        df = pd.read_csv(path)
        df["estado_v2"] = df.apply(nuevo_estado, axis=1)
        df.to_csv(f"datos_reclasificados/{nombre}_v2.csv", index=False)
        ok0 = int((df.estado_parseo == "ok").sum())
        naia = int((df.estado_v2 == "no_aplica_ia").sum())
        resumen.append({"archivo": nombre, "filas": len(df), "ok_original": ok0,
                        "no_aplica_ia": naia, "pct": round(100*naia/ok0, 1) if ok0 else 0})
    r = pd.DataFrame(resumen)
    r.to_csv("datos_reclasificados/RESUMEN_no_aplica_ia.csv", index=False)
    print(r.to_string(index=False))
