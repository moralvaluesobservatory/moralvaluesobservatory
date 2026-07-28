from pathlib import Path
import hashlib, re, sys
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
REG=pd.read_csv(ROOT/"data/metadata/ola2_instrument_registry.csv")

def norm(s): return re.sub(r"\s+"," ",str(s).replace("’", "'").replace("‘", "'").replace("“",'"').replace("”",'"')).strip()
def h(s): return hashlib.sha256(norm(s).encode("utf-8")).hexdigest()
if len(sys.argv)!=2:
    raise SystemExit("Usage: python validate_private_meindl_file.py /path/to/instrumento_privado.csv")
p=Path(sys.argv[1]); d=pd.read_csv(p)
required={"item_id","texto"}
if not required.issubset(d.columns): raise SystemExit(f"Missing columns: {required-set(d.columns)}")
check=d[["item_id","texto"]].copy(); check["observed_hash"]=check.texto.map(h)
m=REG[["item_id","administered_text_sha256"]].merge(check,on="item_id",how="outer",indicator=True)
m["hash_ok"]=m.administered_text_sha256.eq(m.observed_hash)
print(m[["item_id","_merge","hash_ok"]].to_string(index=False))
if len(d)!=65 or not (m._merge.eq("both") & m.hash_ok).all(): raise SystemExit(1)
print("Private instrument matches all 65 expected identifiers and hashes.")
