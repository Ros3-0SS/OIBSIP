import nbformat
from pathlib import Path

nb_path = Path("DataAnalytics-L1-EDARetailSales/EDA_Retail_Sales.ipynb")
nb = nbformat.read(nb_path, as_version=4)

replacements = {
    "fig, ax = plt.subplots(figsize=(12, 5))": "fig, ax = plt.subplots(figsize=(14, 6), constrained_layout=True)",
    "fig, ax = plt.subplots(figsize=(10, 5))": "fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)",
    "fig, ax = plt.subplots(figsize=(10, 6))": "fig, ax = plt.subplots(figsize=(12, 7), constrained_layout=True)",
    "fig, ax = plt.subplots(figsize=(7, 5))": "fig, ax = plt.subplots(figsize=(8, 6), constrained_layout=True)",
    "monthly_revenue.plot(ax=ax, marker='o')": "monthly_revenue.plot(ax=ax, marker='o', linewidth=2, markersize=5)",
    "monthly_aov.plot(ax=ax, marker='o')": "monthly_aov.plot(ax=ax, marker='o', linewidth=2, markersize=5)",
    "ax.tick_params(axis='x', rotation=45)": "ax.tick_params(axis='x', rotation=45, labelsize=9)\nax.grid(axis='y', alpha=0.25)",
    "ax.tick_params(axis='x', rotation=0)": "ax.tick_params(axis='x', rotation=0, labelsize=9)\nax.grid(axis='y', alpha=0.25)",
    "sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', ax=ax)": "sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', linewidths=0.5, square=True, ax=ax)",
}

for cell in nb.cells:
    if cell.cell_type == "code":
        src = cell.source
        for old, new in replacements.items():
            src = src.replace(old, new)
        if "display(fig)" in src and "plt.show()" not in src:
            src = src.replace("display(fig)", "display(fig)\nplt.show()")
        cell.source = src

insert_at = None
for i, cell in enumerate(nb.cells):
    if cell.cell_type == "markdown" and "## 3. Monthly and quarterly sales trends" in cell.source:
        insert_at = i
        break

if insert_at is not None and not any(
    c.cell_type == "markdown" and "Visualisation standards" in c.source for c in nb.cells
):
    note = nbformat.v4.new_markdown_cell(
        "## Visualisation standards\n\n"
        "All business charts are rendered directly in this notebook and saved to `outputs/` at high resolution. "
        "Chart sizes, labels, axis spacing and gridlines are tuned for readability. Each visual is followed immediately "
        "by an observation and a business implication so the analysis is self-contained."
    )
    nb.cells.insert(insert_at, note)

nbformat.write(nb, nb_path)
print(f"Updated {nb_path}")
