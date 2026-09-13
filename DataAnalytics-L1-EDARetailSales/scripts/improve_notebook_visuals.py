import argparse
from pathlib import Path

import nbformat


NB_PATH = Path("DataAnalytics-L1-EDARetailSales/EDA_Retail_Sales.ipynb")


def clean_interpretation_markdown(cell):
    """Remove decorative labels from interpretation cells."""
    if cell.cell_type != "markdown":
        return
    text = cell.source.strip()
    text = text.replace("**📌 Observation:** ", "")
    text = text.replace("**💼 Business implication:** ", "")
    text = text.replace("**Interpretation:** ", "")
    cell.source = text


def remove_repeated_markdown_cells(nb):
    """Remove consecutive duplicate Markdown cells so the notebook stays idempotent."""
    cleaned = []
    previous_markdown = None

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            clean_interpretation_markdown(cell)
            current = cell.source.strip()
            if current and current == previous_markdown:
                continue
            previous_markdown = current
        else:
            previous_markdown = None
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

    new_cells = []
    i = 0
    while i < len(nb.cells):
        cell = nb.cells[i]
        if cell.cell_type != "code":
            clean_interpretation_markdown(cell)
            new_cells.append(cell)
            i += 1
            continue

        src = cell.source
        for old, new in replacements.items():
            src = src.replace(old, new)
        src = src.replace("from IPython.display import display, Markdown\n", "")
        src = src.replace("display(fig)\nplt.show()", "display(fig)")
        src = src.replace("\nplt.show()", "")

        if "display(Markdown(" in src:
            parts = []
            current = []
            for line in src.splitlines(True):
                if "display(Markdown(" in line:
                    if current:
                        parts.append("".join(current).strip())
                        current = []
                    continue
                current.append(line)
            if current:
                parts.append("".join(current).strip())

            interpretations = []
            j = i + 1
            while j < len(nb.cells) and len(interpretations) < len(parts):
                if nb.cells[j].cell_type == "markdown":
                    clean_interpretation_markdown(nb.cells[j])
                    interpretations.append(nb.cells[j])
                    j += 1
                else:
                    break

            for k, part in enumerate(parts):
                if part:
                    new_cells.append(nbformat.v4.new_code_cell(part))
                    if k < len(interpretations):
                        new_cells.append(interpretations[k])
            i = j if len(interpretations) == len(parts) else i + 1
            continue

        cell.source = src
        new_cells.append(cell)
        i += 1

    nb.cells = new_cells
    remove_repeated_markdown_cells(nb)

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
    """Move any remaining rendered Markdown observations into clean Markdown cells."""
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
                markdown_text = "".join(markdown_data) if isinstance(markdown_data, list) else markdown_data
                markdown_text = markdown_text.strip().replace("**📌 Observation:** ", "").replace("**💼 Business implication:** ", "").replace("**Interpretation:** ", "")
                markdown_cells.append(nbformat.v4.new_markdown_cell(markdown_text))
                moved += 1
            else:
                remaining_outputs.append(output)

        cell.outputs = remaining_outputs
        new_cells.append(cell)
        new_cells.extend(markdown_cells)

    nb.cells = new_cells
    remove_repeated_markdown_cells(nb)
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
