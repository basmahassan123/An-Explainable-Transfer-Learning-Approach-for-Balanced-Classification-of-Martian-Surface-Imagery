# GitHub publication checklist

- [ ] Confirm the notebook contains no credentials, API keys, private paths, or private data.
- [ ] Confirm dataset redistribution terms; do not commit dataset images/CSVs unless allowed.
- [ ] Run `python environment_check.py` in the environment used for experiments and save the output with your experiment records.
- [ ] Review the notebook's multiple training sections before execution; do not blindly run all cells.
- [ ] Complete any required class-exclusion rationale from verified dataset provenance.
- [ ] Verify that the notebook's configured paths match the dataset layout described in `data/README.md`.
- [ ] Add a software license only after confirming you have the rights to do so.
- [ ] Add the final manuscript citation/DOI to `CITATION.cff` and README when available.
- [ ] Check the Git diff and repository file list before making the repository public.
