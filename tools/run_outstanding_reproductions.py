from __future__ import annotations

import argparse
import sys
import time
import traceback
from pathlib import Path


WORLD_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORLD_ROOT))

from outstanding_reproductions import BATCH1_CASE_IDS, BATCH2_CASE_IDS, CASES, FORMAL_CASE_IDS, run_case


def progress_bar(done: int, total: int, width: int = 28) -> str:
    filled = int(width * done / max(total, 1))
    return "[" + "#" * filled + "." * (width - filled) + f"] {done}/{total}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run selected outstanding-paper reproductions.")
    parser.add_argument("cases", nargs="*", help="Case ids to run. Empty means run all configured cases.")
    parser.add_argument("--list", action="store_true", help="List available case ids and exit.")
    parser.add_argument("--formal", action="store_true", help="Run the 15 officially documented BAO reproductions.")
    parser.add_argument("--batch", choices=["1", "2"], help="Run one documented reproduction batch.")
    parser.add_argument("--keep-going", action="store_true", help="Continue running remaining cases after a failure.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.cases:
        selected = args.cases
    elif args.batch == "1":
        selected = BATCH1_CASE_IDS
    elif args.batch == "2":
        selected = BATCH2_CASE_IDS
    elif args.formal:
        selected = FORMAL_CASE_IDS
    else:
        selected = list(CASES)

    if args.list:
        for case_id in selected:
            meta = CASES[case_id]
            print(f"{case_id}\t{meta['contest']}\t{meta['year']}-{meta['code']}\t{meta['paper_id']}")
        return 0
    unknown = [case_id for case_id in selected if case_id not in CASES]
    if unknown:
        print("Unknown case id(s): " + ", ".join(unknown), file=sys.stderr)
        return 2

    total = len(selected)
    failures: list[str] = []
    started_all = time.time()
    print(f"Running {total} outstanding-paper reproduction(s)")
    for index, case_id in enumerate(selected, start=1):
        meta = CASES[case_id]
        started = time.time()
        print(f"{progress_bar(index - 1, total)} start {case_id} -> {meta['output']}", flush=True)
        try:
            result = run_case(case_id)
        except Exception:
            failures.append(case_id)
            print(f"{progress_bar(index, total)} failed {case_id}", file=sys.stderr, flush=True)
            traceback.print_exc()
            if not args.keep_going:
                break
        else:
            elapsed = time.time() - started
            print(
                f"{progress_bar(index, total)} done {case_id} in {elapsed:.1f}s; result={meta['output'] / 'result.json'}",
                flush=True,
            )
            if "target_comparison" in result:
                print(f"  comparisons: {', '.join(result['target_comparison'].keys())}", flush=True)
    elapsed_all = time.time() - started_all
    if failures:
        print(f"Finished with {len(failures)} failure(s) in {elapsed_all:.1f}s: {', '.join(failures)}", file=sys.stderr)
        return 1
    print(f"All {total} reproduction(s) finished in {elapsed_all:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
