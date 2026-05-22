from __future__ import annotations

import sys
from pathlib import Path


REAL_SOLUTIONS_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(REAL_SOLUTIONS_ROOT))

from statement_workflows import run_2018_icm_f


PROBLEM_TITLE = "Cost of Privacy"
PI_DOMAINS = "defined in statement_workflows.py"
DATA_ELEMENTS = "defined in statement_workflows.py"


def main() -> None:
    run_2018_icm_f(Path(__file__))


if __name__ == "__main__":
    main()
