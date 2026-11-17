"""Сохранение артефактов этапа: графики -> reports/figures, таблицы -> reports/tables."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "reports" / "figures"
TAB_DIR = ROOT / "reports" / "tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TAB_DIR.mkdir(parents=True, exist_ok=True)

def save_fig(fig_or_ax, name, dpi=150, show=True):
    """Сохранить график в reports/figures/<name>.png. Принимает fig или ax."""
    fig = fig_or_ax if isinstance(fig_or_ax, Figure) else fig_or_ax.figure
    path = FIG_DIR / f"{name}.png"
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)

def save_table(df, name):
    """Сохранить таблицу в reports/tables/<name>.csv (UTF-8 с BOM, без индекса)."""
    path = TAB_DIR / f"{name}.csv"
    df.to_csv(path, index=False, encoding="utf-8-sig")