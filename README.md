# What Drives xG?

**Question:** How much of StatsBomb's xG can be recovered from public shot data, and which inputs matter most?

This project builds an expected-goals (xG) model on StatsBomb Open Data and measures how much of the gap between a simple distance-and-angle baseline and StatsBomb's own xG each additional feature group closes. The result is an honest finding about which shot attributes carry predictive information, not a leaderboard score.

> **Status:** Checkpoint 0 complete — scaffolding only. No results yet.

---

## What this project does not do

- It does not claim to beat StatsBomb's xG model.
- It does not reproduce StatsBomb's model; it builds an independent model on the same open data.
- All numbers in this README come from output files produced by code in this repo. Placeholders are clearly marked.

---

## Data

Source: [StatsBomb Open Data](https://github.com/statsbomb/open-data) via the `statsbombpy` Python library.

StatsBomb's data is used under their open data user agreement. Data files are not committed to this repository. See [StatsBomb Open Data Terms](https://github.com/statsbomb/open-data/blob/master/LICENSE.pdf) for terms of use.

**Competitions used:** `[PLACEHOLDER — to be filled after checkpoint 1]`

**Held-out competitions for transfer test:** `[PLACEHOLDER — to be filled after checkpoint 1]`

---

## Method summary

Feature groups are added cumulatively:

| Group | Features |
|-------|----------|
| 1 — Baseline | Distance to goal, angle to goal, visible goal angle |
| 2 — Shot attributes | Body part, shot type, technique |
| 3 — Context | Play pattern, first time, under pressure, one-on-one, and similar flags |
| 4 — Freeze frame | Defenders in shooting cone, goalkeeper position/distance, nearest defender distance |

Models: logistic regression and regularized gradient boosting (LightGBM) at each stage.

**Headline metric:** fraction of gap closed = (baseline log loss − model log loss) / (baseline log loss − StatsBomb xG log loss), measured on the same shots.

Exclusions: penalties and shootout shots are removed from the main model.

---

## Results

`[PLACEHOLDER — all results tables and figures will be linked here after the respective checkpoints are complete]`

---

## Repo layout

```
what-drives-xg/
  README.md            — this file
  requirements.txt     — pinned Python dependencies
  config.yaml          — competitions, seeds, paths
  .gitignore
  data/                — gitignored; populated by scripts at runtime
  src/                 — library code (loading, features, evaluation, leakage policy)
  scripts/             — numbered scripts, one per modelling step
  tests/               — unit tests (geometry features, leakage policy)
  results/             — CSVs, JSONs, PNGs committed; large caches gitignored
  docs/                — findings.md and supporting notes
```

---

## Reproducing the analysis

### 1. Set up

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run the pipeline

Scripts are numbered in order. Each script accepts `--config config.yaml` and `--smoke` for a quick crash-check.

```
[PLACEHOLDER — full commands listed after each checkpoint is complete]
```

---

## Limitations

- StatsBomb's xG may have been trained on these same shots; the gap-closed metric reflects that.
- The open-data xG values may correspond to an older model version than StatsBomb's current product.
- Freeze-frame data is only available for some competitions; group 4 features cover a subset of shots.
- Feature-group credit depends on ordering; we average over multiple orderings and report bootstrap confidence intervals.

---

## Credit

Data provided by StatsBomb under their open data user agreement.

> "StatsBomb Open Data is provided free of charge for public non-commercial use."

See [https://github.com/statsbomb/open-data](https://github.com/statsbomb/open-data) for the full licence and terms.
