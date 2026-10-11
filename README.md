# An Explainable Transfer Learning Approach for Balanced Classification of Martian Surface Imagery

This repository contains the computational notebook accompanying the manuscript. The implementation uses VGG16 transfer learning for Martian surface image classification and includes evaluation and reviewer-oriented analyses such as class-wise metrics, confusion matrices, ROC/precision–recall curves, ablation experiments, repeated-seed evaluation, and Grad-CAM visualizations where supported by the supplied data and code.

## Repository contents

- `Martian_Surface_Imagery_Revision.ipynb` — notebook containing the main pipeline, evaluation utilities, and additional reviewer experiments.
- `requirements.txt` — Python dependencies.
- `environment_check.py` — reports Python/package versions and whether TensorFlow detects a GPU.
- `data/README.md` — expected local dataset layout and CSV schema.
- `CITATION.cff` — citation metadata.
- `.gitignore` — excludes datasets, generated results, model checkpoints, logs, and local environments.

## Important before running

1. **The dataset is not included.** Obtain it from the source permitted by its owner and follow its applicable terms. Do not upload images or derived data unless you have permission to redistribute them.
2. The notebook expects `Train_CSV.csv`, `Validation_CSV.csv`, and `Test_CSV.csv` in the dataset directory. Each CSV must contain `JPG` and `LABELS` columns. The `JPG` values must resolve to image files relative to that dataset directory.
3. The notebook contains multiple training and reviewer-experiment sections. Do **not** select “Run All” without reviewing the cell order and compute cost: some cells train a full model, while later cells run additional experiments or expect a previously trained model/checkpoint.
4. The code can create large output directories, checkpoints, and figures. Keep these local; the repository `.gitignore` excludes them.
5. The code contains an `EXCLUSION_RATIONALE`/class-selection item that must be completed from documented dataset provenance if the corresponding experiment/report requires it. Do not invent a scientific reason for excluded classes.
6. Reproducibility is affected by TensorFlow/Keras versions, GPU availability, and nondeterministic GPU kernels. Record the versions printed by `environment_check.py` alongside any reported run.

## Environment

The intended environment is Python 3.11. Install dependencies in a fresh virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python environment_check.py
jupyter notebook
```

If PowerShell blocks activation, use the activation method permitted by your system policy or run the environment's Python executable directly.

## Dataset placement

By default, place the dataset files and images under:

```text
data/
└── Mars Surface and Curiosity Image/
    ├── Train_CSV.csv
    ├── Validation_CSV.csv
    ├── Test_CSV.csv
    └── ... image files referenced by the JPG column ...
```

The notebook's main pipeline uses this relative location. Some later reviewer-experiment cells may use their own configuration variables; inspect those cells and ensure they point to the same dataset and desired output directory before running them.

## Outputs

The notebook may generate figures, CSV/Excel tables, logs, Grad-CAM images, and saved model checkpoints. By default, generated results should remain in `results/` and are not intended to be committed to GitHub.

## Hardware and GPU notes

The original experiments were conducted on Windows 11 with Python 3.11, an Intel Core i7-10750H CPU, 32 GB RAM, and an NVIDIA RTX 3000 GPU with 6 GB memory. TensorFlow GPU support depends on the installed TensorFlow build and runtime configuration. On native Windows, modern TensorFlow versions generally do not provide CUDA GPU execution; GPU execution may require a compatible WSL2/Linux setup. Verify actual device detection using `python environment_check.py` rather than assuming the GPU is active.

## License and data rights

No software license is asserted by this repository template. Before making the repository public, choose and add a license only if you have the rights to license the code. Dataset licensing and redistribution rights are separate from the code license.
