from __future__ import annotations

import sys
from pathlib import Path


REAL_SOLUTIONS_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(REAL_SOLUTIONS_ROOT))

from statement_workflows import run_2018_icm_d


PROBLEM_TITLE = "Out of Gas and Driving on E"
EV_ADOPTION_LEVELS = "defined in statement_workflows.py"
REGION_TYPES = "defined in statement_workflows.py"


def main() -> None:
    run_2018_icm_d(Path(__file__))


if __name__ == "__main__":
    main()
