# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
solutions = sorted((ROOT / "question_solutions").glob("*/*/q*/solution.py"))
failures = []
for solution in solutions:
    print(f"[run-question] {solution.relative_to(ROOT)}")
    completed = subprocess.run([sys.executable, str(solution)], cwd=str(ROOT.parents[0]))
    if completed.returncode != 0:
        failures.append(str(solution))
if failures:
    print("Failures:")
    for item in failures:
        print(item)
    raise SystemExit(1)
print(f"Completed {len(solutions)} per-question CUMCM experiments.")
