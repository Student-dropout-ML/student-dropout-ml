#\!/usr/bin/env python3
"""
run_all.py — Spusti vsechny notebooky projektu poporade.

Pouziti:
    python run_all.py              # spusti vse
    python run_all.py --from 03d   # zacne od konkretniho notebooku
    python run_all.py --only 04a 04b  # spusti jen vybrane notebooky

Vystupy se zapisuji zpet do .ipynb (bunky se naplni vystupy).
"""

import subprocess
import sys
import time
import shutil
from pathlib import Path

# ── Poradi notebooku ─────────────────────────────────────────────────────────
NOTEBOOKS = [
    "01-exploratory-data-analysis.ipynb",
    "02-data-preprocessing.ipynb",
    "03a-dummy-baseline.ipynb",
    "03b-baseline-models.ipynb",
    "03c-baseline-evaluation.ipynb",
    "03d-hyperparameter-tuning.ipynb",
    "04a-clustering-model.ipynb",
    "04b-clustering-evaluation.ipynb",
    "05-model-evaluation.ipynb",
    "06a-xai-setup.ipynb",
    "06b-shap-n-ice-global.ipynb",
    "06c-shap-local.ipynb",
    "06d-lime-explanations.ipynb",
    "06e-xai-cross-comparison.ipynb",
    "06f-decision-tree-explanation.ipynb",
]

# ── Parsovani argumentu ──────────────────────────────────────────────────────
args = sys.argv[1:]
start_from = None
only = []

i = 0
while i < len(args):
    if args[i] == "--from" and i + 1 < len(args):
        start_from = args[i + 1]
        i += 2
    elif args[i] == "--only":
        i += 1
        while i < len(args) and not args[i].startswith("--"):
            only.append(args[i])
            i += 1
    else:
        i += 1

notebooks_dir = Path(__file__).parent / "notebooks"

# Najdi jupyter
jupyter_path = shutil.which("jupyter") or str(Path.home() / ".local/bin/jupyter")

# ── Vyber ktere notebooky spustit ────────────────────────────────────────────
to_run = list(NOTEBOOKS)

if only:
    to_run = [nb for nb in NOTEBOOKS if any(pat in nb for pat in only)]
elif start_from:
    idx = next((j for j, nb in enumerate(NOTEBOOKS) if start_from in nb), None)
    if idx is None:
        print(f"ERROR: '{start_from}' nenalezen v seznamu notebooku.")
        sys.exit(1)
    to_run = NOTEBOOKS[idx:]

# ── Spusteni ─────────────────────────────────────────────────────────────────
sep = "=" * 60
print(f"\n{sep}")
print(f"  Spoustim {len(to_run)} notebooku")
print(f"{sep}\n")

results = []
total_start = time.time()

for nb in to_run:
    nb_path = notebooks_dir / nb
    if not nb_path.exists():
        print(f"  --  PRESKAKUJI (nenalezen): {nb}")
        results.append((nb, "skip", 0))
        continue

    print(f"  >>  {nb} ...", end=" ", flush=True)
    t0 = time.time()

    proc = subprocess.run(
        [
            jupyter_path, "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=600",
            "--ExecutePreprocessor.kernel_name=python3",
            str(nb_path),
        ],
        capture_output=True,
        text=True,
    )

    elapsed = time.time() - t0

    if proc.returncode == 0:
        print(f"OK  ({elapsed:.0f}s)")
        results.append((nb, "ok", elapsed))
    else:
        print(f"CHYBA  ({elapsed:.0f}s)")
        for line in proc.stderr.strip().splitlines()[-10:]:
            print(f"     {line}")
        results.append((nb, "error", elapsed))
        short = nb.replace(".ipynb", "")
        print(f"\n  Zastavuji -- oprav chybu v {nb} a spust znovu:")
        print(f"    python run_all.py --from {short}\n")
        break

# ── Souhrn ───────────────────────────────────────────────────────────────────
total = time.time() - total_start
print(f"\n{sep}")
print(f"  Souhrn  (celkem {total:.0f}s)")
print(f"{sep}")
for nb, status, elapsed in results:
    icon = {"ok": "OK   ", "error": "CHYBA", "skip": "--   "}.get(status, "?    ")
    if status == "skip":
        print(f"  {icon}  {nb}  (preskoceno)")
    else:
        print(f"  {icon}  {nb:<50s}  {elapsed:.0f}s")

ok_count  = sum(1 for _, s, _ in results if s == "ok")
err_count = sum(1 for _, s, _ in results if s == "error")
skipped   = len(to_run) - ok_count - err_count
print(f"\n  {ok_count} OK  |  {err_count} chyb  |  {skipped} preskoceno")
