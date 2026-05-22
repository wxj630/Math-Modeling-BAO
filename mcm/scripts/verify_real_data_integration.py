from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
index = json.loads((ROOT / "question_solution_index.json").read_text(encoding="utf-8"))
if not index:
    errors.append("empty question_solution_index.json")
for row in index:
    for key in ("solution_path", "result_path", "report_path", "artifact_path"):
        if not (ROOT / row[key]).exists():
            errors.append(f"missing {key}: {row[key]}")
    result = json.loads((ROOT / row["result_path"]).read_text(encoding="utf-8"))
    if result.get("data_source", {}).get("type") != row.get("source_type"):
        errors.append(f"{row['problem_id']} source type mismatch")
manifest = json.loads((ROOT / "data_manifest.json").read_text(encoding="utf-8"))
if not any(item.get("problem_id") == "2015-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2015-C official statement pdf")
if not any(item.get("problem_id") == "2015-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2015-D official statement pdf")
if not any(item.get("problem_id") == "2015-D" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2015-D World Bank csv assets")
if not any(item.get("problem_id") == "2016-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-A official statement pdf")
if not any(item.get("problem_id") == "2016-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-B official statement pdf")
if not any(item.get("problem_id") == "2016-C" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2016-C xlsx assets")
if not any(item.get("problem_id") == "2016-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-D official statement pdf")
if not any(item.get("problem_id") == "2016-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-E official statement pdf")
if not any(item.get("problem_id") == "2016-E" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2016-E World Bank csv assets")
if not any(item.get("problem_id") == "2016-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-F official statement pdf")
if not any(item.get("problem_id") == "2016-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2016-C official statement/pdf assets")
if not any(item.get("problem_id") == "2017-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2017-A official statement pdf")
if not any(item.get("problem_id") == "2017-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2017-B official statement pdf")
if not any(item.get("problem_id") == "2017-D" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2017-D xlsx assets")
if not any(item.get("problem_id") == "2017-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2017-D official statement pdf")
if not any(item.get("problem_id") == "2017-C" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2017-C xlsx assets")
if not any(item.get("problem_id") == "2017-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2017-C official statement pdf")
if not any(item.get("problem_id") == "2018-C" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2018-C xlsx assets")
if not any(item.get("problem_id") == "2018-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2018-C official statement pdf")
if not any(item.get("problem_id") == "2019-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-A official statement pdf")
if not any(item.get("problem_id") == "2019-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-B official statement pdf")
if not any(item.get("problem_id") == "2019-C" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2019-C xlsx assets")
if not any(item.get("problem_id") == "2019-C" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2019-C csv assets")
if not any(item.get("problem_id") == "2019-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-C official statement pdf")
if not any(item.get("problem_id") == "2019-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-D official statement pdf")
if not any(item.get("problem_id") == "2019-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-E official statement pdf")
if not any(item.get("problem_id") == "2019-P06" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2019-P06 official statement pdf")
if not any(item.get("problem_id") == "2020-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-A official statement pdf")
if not any(item.get("problem_id") == "2020-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-B official statement pdf")
if not any(item.get("problem_id") == "2020-C" and item.get("kind") == "zip" for item in manifest):
    errors.append("data manifest missing 2020-C official tsv zip assets")
if not any(item.get("problem_id") == "2020-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-C official statement pdf")
if not any(item.get("problem_id") == "2020-D" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2020-D csv assets")
if not any(item.get("problem_id") == "2020-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-D official statement pdf")
if not any(item.get("problem_id") == "2020-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-E official statement pdf")
if not any(item.get("problem_id") == "2020-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2020-F official statement pdf")
if not any(item.get("problem_id") == "2021-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-A official statement pdf")
if not any(item.get("problem_id") == "2021-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-B official statement pdf")
if not any(item.get("problem_id") == "2021-C" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2021-C xlsx assets")
if not any(item.get("problem_id") == "2021-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-C official statement pdf")
if not any(item.get("problem_id") == "2021-D" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2021-D csv assets")
if not any(item.get("problem_id") == "2021-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-D official statement pdf")
if not any(item.get("problem_id") == "2021-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-E official statement pdf")
if not any(item.get("problem_id") == "2021-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2021-F official statement pdf")
if not any(item.get("problem_id") == "2022-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-A official statement pdf")
if not any(item.get("problem_id") == "2022-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-B official statement pdf")
if not any(item.get("problem_id") == "2022-C" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2022-C csv assets")
if not any(item.get("problem_id") == "2022-C" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-C official statement pdf")
if not any(item.get("problem_id") == "2022-P01" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-P01 official statement pdf")
if not any(item.get("problem_id") == "2022-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-E official statement pdf")
if not any(item.get("problem_id") == "2022-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2022-F official statement pdf")
if not any(item.get("problem_id") == "2025-C" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2025-C csv assets")
if not any(item.get("problem_id") == "2024-C" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2024-C csv assets")
if not any(item.get("problem_id") == "2024-D" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2024-D xlsx assets")
if not any(item.get("problem_id") == "2025-D" and item.get("kind") == "csv" for item in manifest):
    errors.append("data manifest missing 2025-D csv assets")
if not any(item.get("problem_id") == "2023-C-Wordle" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2023-C-Wordle xlsx assets")
if not any(item.get("problem_id") == "2023-C-Boats" and item.get("kind") == "xlsx" for item in manifest):
    errors.append("data manifest missing 2023-C-Boats xlsx assets")
if not any(item.get("problem_id") == "2023-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-A official statement pdf")
if not any(item.get("problem_id") == "2023-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-B official statement pdf")
if not any(item.get("problem_id") == "2023-D" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-D official statement pdf")
if not any(item.get("problem_id") == "2023-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-E official statement pdf")
if not any(item.get("problem_id") == "2023-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-F official statement pdf")
if not any(item.get("problem_id") == "2023-F-GreenGDP" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2023-F-GreenGDP official statement pdf")
if not any(item.get("problem_id") == "2024-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2024-A official statement pdf")
if not any(item.get("problem_id") == "2024-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2024-B official statement pdf")
if not any(item.get("problem_id") == "2024-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2024-E official statement pdf")
if not any(item.get("problem_id") == "2024-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2024-F official statement pdf")
if not any(item.get("problem_id") == "2025-A" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2025-A official statement pdf")
if not any(item.get("problem_id") == "2025-B" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2025-B official statement pdf")
if not any(item.get("problem_id") == "2025-E" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2025-E official statement pdf")
if not any(item.get("problem_id") == "2025-F" and item.get("kind") == "pdf" for item in manifest):
    errors.append("data manifest missing 2025-F official statement pdf")
print(f"real question solutions: {len(index)}")
print(f"data manifest rows: {len(manifest)}")
print(f"errors: {len(errors)}")
for error in errors[:50]:
    print("ERROR:", error)
if errors:
    raise SystemExit(1)
