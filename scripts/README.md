# scripts/

Numbered scripts — run in order. Each accepts `--config` and `--smoke` flags.

| Script | Checkpoint | Purpose |
|--------|-----------|---------|
| `01_data_audit.py` | 1 | List competitions, count shots, check freeze frames, write `results/data_audit.md` |
| `02_build_pipeline.py` | 2 | Build processed shot table, apply exclusions |
| `03_explore.py` | 3 | Shot maps and goal-rate plots |
| `04_build_features.py` | 4 | All feature groups |
| `05_ablation.py` | 5 | Cumulative ablation, leave-one-group-out, bootstrap |
| `06_ablation_analysis.py` | 6 | Charts and tables from ablation outputs |
| `07_calibration.py` | 7 | Reliability curves, StatsBomb scatter |
| `08_transfer_test.py` | 8 | Train on core, test on held-out |

Scripts are added at their respective checkpoints.
