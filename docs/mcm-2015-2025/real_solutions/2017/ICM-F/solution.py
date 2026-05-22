from __future__ import annotations

import sys
from pathlib import Path


REAL_SOLUTIONS_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(REAL_SOLUTIONS_ROOT))

from statement_workflows import run_2017_icm_f


PROBLEM_TITLE = "Migration to Mars: Utopian Workforce of the 2100 Urban Society"
POPULATION_ZERO_SIZE = 10000
PRIORITY_FACTORS = "defined in statement_workflows.py"
WORKFORCE_GROUPS = "defined in statement_workflows.py"


def main() -> None:
    run_2017_icm_f(Path(__file__))


if __name__ == "__main__":
    main()
