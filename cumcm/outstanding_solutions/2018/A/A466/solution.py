from __future__ import annotations

import sys
from pathlib import Path


WORLD_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(WORLD_ROOT))

from outstanding_reproductions import run_case


if __name__ == "__main__":
    run_case("cumcm-2018-A-A466", Path(__file__).resolve().parent)
