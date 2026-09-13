import argparse
from pathlib import Path

import nbformat


NB_PATH = Path("DataAnalytics-L1-EDARetailSales/EDA_Retail_Sales.ipynb")


def remove_old_interpretations(nb):
    """Remove interpretation cells created by an earlier post-processing run."""
    cleaned = []
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            text = cell.source.strip()
            if text.startswith("**Interpretation:**") or text.startswith("Interpretation:"):
                continue
        cleaned.append(cell)
    nb.cells = cleaned


def refresh_visuals(nb):
    replacements = {
        "fig, ax = plt.subplots(figsize=(12, 5))": "fig, ax = plt.subplots(figsize=(14, 6))",
        "fig, ax = plt.subplots(figsize=(10, 5))": "fig, ax = plt.subplots(figsize=(12, 6))",
        "fig, ax = plt.subplots(figsize=(10, 6))": "fig, ax = plt.subplots(figsize=(12, 7))",
        "fig, ax = plt.subplots(figsize=(7, 5))": "fig, ax = plt.subplots(figsize=(8, 6))",
        "fig, ax = plt.subplots(figsize=(14, 6), constrained_layout=True)": "fig, ax = plt.subplots(figsize=(14, 6))",
        "fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)": "fig, ax = plt.subplots(figsize=(12, 6))",
        "fig, ax = plt.subplots(figsize=(12, 7), constrained_layout=True)": "fig, ax = plt.subplots(figsize=(12, 7))",
        "fig, ax = plt.subplots(figsize=(8, 6), constrained_layout=True)": "fig, ax = plt.subplots(figsize=(8, 6))",
        "monthly_revenue.plot(ax=ax, marker='o')": "monthly_revenue.plot(ax=ax, marker='o', linewidth=2, markersize=5)",
        "monthly_aov.plot(ax=ax, marker='o')": "monthly_aov.plot(ax=ax, marker='o', linewidth=2, markersize=5)",
        "ax.tick_params(axis='x', rotation=45)": "ax.tick_params(axis='x', rotation=45, labelsize=9)\nax.grid(axis='y', alpha=0.25)",
        "ax.tick_params(axis='x', rotation=0)": "ax.tick_params(axis='x', rotation=0, labelsize=9)\nax.grid(axis='y', alpha=0.25)",
        "sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', ax=ax)": "sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', linewidths=0.5, square=True, ax=ax)",
    }

    remove_old_interpretations(nb)

    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        src = cell.source
        for old, new in replacements.items():
            src = src.replace(old, new)

        # Do not add plt.show() after display(fig): in Jupyter this renders the
        # same figure twice. display(fig) is sufficient for the embedded output.
        src = src.replace("display(fig)\nplt.show()", "display(fig)")
        cell.source = src

    if not any(
        c.cell_type == "markdown" and "Visualisation standards" in c.source
        for c in nb.cells
    ):
        insert_at = next(
            (
                i
                for i, cell in enumerate(nb.cells)
                if cell.cell_type == "markdown"
                and "## 3. Monthly and quarterly sales trends" in cell.source
            ),
            None,
        )
        if insert_at is not None:
            note = nbformat.v4.new_markdown_cell(
                "## Visualisation standards\n\n"
                "All business charts are rendered directly in this notebook and saved to `outputs/` at high resolution. "
                "Chart sizes, labels, axis spacing and gridlines are tuned for readability. Each visual is followed immediately "
                "by its own interpretation and business implication."
            )
            nb.cells.insert(insert_at, note)


def split_interpretation_outputs(nb):
    """Move rendered Markdown observations into clean Markdown cells.

    The final notebook order is visual/table -> interpretation -> next visual/table.
    Existing interpretation cells are removed first so repeated workflow runs cannot
    duplicate them.
    """
    remove_old_interpretations(nb)
    new_cells = []
    moved = 0

    for cell in nb.cells:
        if cell.cell_type != "code" or not cell.get("outputs"):
            new_cells.append(cell)
            continue

        markdown_cells = []
        remaining_outputs = []
        for output in cell.outputs:
            markdown_data = output.get("data", {}).get("text/markdown")
            if markdown_data:
                if isinstance(markdown_data, list):
                    markdown_text = "".join(markdown_data)
                else:
                    markdown_text = markdown_data

                # Keep the interpretation as clean prose rather than a decorated heading.
                markdown_text = markdown_text.strip()
                if markdown_text.startswith("**Interpretation:**"):
                    markdown_text = markdown_text[len("**Interpretation:**"):].strip()
                elif markdown_text.startswith("Interpretation:"):
                    markdown_text = markdown_text[len("Interpretation:"):].strip()

                markdown_cells.append(nbformat.v4.new_markdown_cell(markdown_text))
                moved += 1
            else:
                remaining_outputs.append(output)

        cell.outputs = remaining_outputs
        new_cells.append(cell)
        new_cells.extend(markdown_cells)

    nb.cells = new_cells
    return moved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--postprocess",
        action="store_true",
        help="After execution, move rendered Markdown interpretations into separate Markdown cells.",
    )
    args = parser.parse_args()

    nb = nbformat.read(NB_PATH, as_version=4)

    if args.postprocess:
        moved = split_interpretation_outputs(nb)
        nbformat.write(nb, NB_PATH)
        print(f"Moved {moved} interpretation(s) into separate clean Markdown cells in {NB_PATH}")
    else:
        refresh_visuals(nb)
        nbformat.write(nb, NB_PATH)
        print(f"Updated {NB_PATH}")


if __name__ == "__main__":
    main()
