from __future__ import annotations

import sys
from pathlib import Path


REAL_SOLUTIONS_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(REAL_SOLUTIONS_ROOT))

from statement_workflows import run_2018_mcm_a


PROBLEM_TITLE = "Multi-hop HF Radio Propagation"
EARTH_RADIUS_KM = "defined in statement_workflows.py"
IONOSPHERE_HEIGHT_KM = "defined in statement_workflows.py"


def main() -> None:
    run_2018_mcm_a(Path(__file__))


if __name__ == "__main__":
    main()
