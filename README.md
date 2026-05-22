# Math-Modeling-World

Math-Modeling-World bundles a MathModeling agent that couples `kimi-agent-sdk`, a local agent spec, and Jupyter-backed execution tools inspired by `MathModelAgent`.

## Installation

1. Activate the provided virtual environment: `source .venv/bin/activate`.
2. Install the agent and its dependencies in editable mode: `uv pip install -e .`.
3. Make sure `.env` contains `KIMI_BASE_URL`, `KIMI_API_KEY`, and optionally `KIMI_MODEL_NAME` (defaults to `kimi-k2.5`).

## Usage

```bash
mm-world-agent --prompt "Analyze the competition problem" --port 8888
```

The runner prints the `http://0.0.0.0:<port>` URL so you can open Jupyter Lab (default port 8888, override via `--port` or `MATH_MODELING_JUPYTER_PORT`). The MathModeling agent loads the local `src/mm_world/agents/agent.yaml` spec, dispatches the Modeler/Coder/Writer workflow, and keeps detailed logs in `logs/`.

For dry runs or to inspect the logs without executing code, pass `--dry-run`. Use `--no-yolo` if you want to handle approval requests manually.

## Development Notes

- The custom tools live under `src/mm_world/tools` and include a Jupyter-based local interpreter plus an OpenAlex scholar helper with a `search_enabled` toggle.
- The custom agent spec exists in `src/mm_world/agents`, extends `default`, and wires Markdown-based Modeler/Coder/Writer prompts to orchestrate the workflow.

## GitHub Pages Tutorial

The tutorial site follows the VitePress structure used by `/Users/wuxiaojun/code/repo-template`.

- Entry page: [`docs/index.md`](docs/index.md)
- Learning route: [`docs/tutorial`](docs/tutorial/)
- MCM/ICM tutorial: [`docs/mcm-track`](docs/mcm-track/)
- CUMCM tutorial: [`docs/cumcm-track`](docs/cumcm-track/)
- Reproduction guide: [`docs/reference/reproduce.md`](docs/reference/reproduce.md)

Run the tutorial locally with:

```bash
npm install
npm run docs:dev
```

Build the GitHub Pages artifact with:

```bash
npm run docs:build
```

## MCM 2015-2025 Archive

The curated MCM/ICM problem notes, model recommendations, runnable Python templates, and captured execution results live in [`docs/mcm-2015-2025`](docs/mcm-2015-2025/README.md).

Regenerate the archive and rerun every solution template with:

```bash
.venv/bin/python scripts/build_mcm_archive.py
```

For each problem, the archive now includes a concrete `solution.py`, `problem_config.json`, `实验结果.md`, `experiment_results.json`, and `experiment_scores.png` generated from the per-question model mapping.

Important correction: the earlier generated MCM `advanced/` and per-problem `solution.py` files used randomly generated smoke-test data and must not be treated as real contest-data solutions. See [`docs/mcm-2015-2025/REALITY_CHECK.md`](docs/mcm-2015-2025/REALITY_CHECK.md) and [`docs/mcm-2015-2025/synthetic_usage_audit.csv`](docs/mcm-2015-2025/synthetic_usage_audit.csv).

Real-data MCM work now starts under [`docs/mcm-2015-2025/real_solutions`](docs/mcm-2015-2025/real_solutions/README.md), using downloaded COMAP official assets in [`docs/mcm-2015-2025/official_assets_extracted`](docs/mcm-2015-2025/official_assets_extracted). The CUMCM-style runnable archive is [`mcm`](mcm/README.md), currently covering `2024-C`, `2024-D`, `2025-C`, and `2025-D` as 24 real-data per-question experiments.
