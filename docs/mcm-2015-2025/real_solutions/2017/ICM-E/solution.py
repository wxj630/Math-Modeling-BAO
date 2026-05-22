from __future__ import annotations

import sys
from pathlib import Path


REAL_SOLUTIONS_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(REAL_SOLUTIONS_ROOT))

from statement_workflows import run_2017_icm_e


PROBLEM_TITLE = "Sustainable Cities Needed!"
SMART_GROWTH_PRINCIPLES = "defined in statement_workflows.py"
SELECTED_CITIES = "defined in statement_workflows.py"


def main() -> None:
    run_2017_icm_e(Path(__file__))


if __name__ == "__main__":
    main()
