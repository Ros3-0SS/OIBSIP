# Fraud Detection Dataset

This project uses the benchmark Credit Card Fraud Detection dataset.

The repository tracks `creditcard.csv` with **Git LFS** because the dataset is large. The working file must have the exact filename:

```text
creditcard.csv
```

The notebook expects the standard columns including `Time`, `Amount`, and target column `Class`, where `1` represents fraud and `0` represents a legitimate transaction.

The committed GitHub file is an LFS pointer; cloning the repository with Git LFS enabled retrieves the actual dataset. This keeps the large dataset out of normal Git object history while preserving a reproducible project structure.