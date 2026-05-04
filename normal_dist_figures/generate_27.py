import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "../data_types_lesson_assets"
BLUE = "#2563eb"
RED = "#dc2626"
GREEN = "#16a34a"
GRAY = "#6b7280"


def bar_chart(ax, labels, values, color, title, xlabel="人数"):
    bars = ax.barh(labels, values, color=color, alpha=0.8, height=0.5)
    for bar, val in zip(bars, values):
        ax.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=11)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlim(0, max(values) * 1.2)


def hist_chart(ax, bins, counts, color, title, xlabel="点数", ylabel="人数", alpha=0.8):
    width = bins[1] - bins[0]
    centers = [(bins[i] + bins[i + 1]) / 2 for i in range(len(bins) - 1)]
    ax.bar(centers, counts, width=width * 0.9, color=color, alpha=alpha, edgecolor="white", linewidth=1.5)
    ax.set_xticks(bins)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_ylim(0, max(counts) * 1.25)


# ── fig01: 棒グラフ（馬券種） ──────────────────────────────────
def fig01_bar_chart():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    labels = ["単勝", "複勝", "馬連", "三連複"]
    values = [12, 8, 15, 20]
    bar_chart(ax, labels, values, BLUE, "好きな馬券種（棒グラフ）")
    fig.tight_layout()
    fig.savefig(f"{OUT}/01_bar_chart.png", bbox_inches="tight")
    plt.close(fig)


# ── fig02: テスト点数ヒストグラム（基本） ─────────────────────────
def fig02_histogram_basic():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    bins = [50, 60, 70, 80, 90, 100]
    counts = [2, 6, 6, 4, 2]
    hist_chart(ax, bins, counts, BLUE, "テスト点数の分布（ヒストグラム）")
    ax.annotate("一番多い区間\n（中心付近）", xy=(65, 6), xytext=(80, 6.5),
                fontsize=9, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY, lw=1))
    fig.tight_layout()
    fig.savefig(f"{OUT}/02_histogram_basic.png", bbox_inches="tight")
    plt.close(fig)


# ── fig03: ばらつきの比較（A vs B） ──────────────────────────────
def fig03_spread_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

    ax = axes[0]
    bins_a = [60, 70, 80, 90]
    counts_a = [3, 10, 3]
    hist_chart(ax, bins_a, counts_a, BLUE, "A：ばらつきが小さい\n（70〜80点に集中）")

    ax = axes[1]
    bins_b = [30, 40, 50, 60, 70, 80, 90, 100]
    counts_b = [2, 2, 2, 2, 2, 2, 2]
    hist_chart(ax, bins_b, counts_b, RED, "B：ばらつきが大きい\n（広い範囲に散らばり）")

    fig.suptitle("ヒストグラムでばらつきを読む", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/03_spread_comparison.png", bbox_inches="tight")
    plt.close(fig)


# ── fig04: 対称な分布 ─────────────────────────────────────────
def fig04_symmetric():
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    bins = [40, 50, 60, 70, 80, 90]
    counts = [2, 4, 6, 4, 2]
    hist_chart(ax, bins, counts, BLUE, "対称な分布")
    ax.axvline(65, color=GRAY, linewidth=1.5, linestyle="--", label="中心")
    ax.legend(fontsize=10)
    ax.text(65, 6.5, "←左右が\nほぼ同じ形→", ha="center", fontsize=9, color=GRAY)
    fig.tight_layout()
    fig.savefig(f"{OUT}/04_symmetric.png", bbox_inches="tight")
    plt.close(fig)


# ── fig05: ベル型の分布 ──────────────────────────────────────
def fig05_bell():
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    bins = [40, 50, 60, 70, 80, 90]
    counts = [1, 3, 6, 3, 1]
    hist_chart(ax, bins, counts, BLUE, "ベル型の分布（正規分布に近い形）")
    ax.axvline(65, color=GRAY, linewidth=1.5, linestyle="--")
    ax.text(65, 6.5, "中央が最も高く\n左右になだらかに下がる", ha="center", fontsize=9, color=GRAY)
    fig.tight_layout()
    fig.savefig(f"{OUT}/05_bell.png", bbox_inches="tight")
    plt.close(fig)


# ── fig06: 一様な分布 ─────────────────────────────────────────
def fig06_uniform():
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    bins = [10, 20, 30, 40, 50, 60]
    counts = [3, 3, 3, 3, 3]
    hist_chart(ax, bins, counts, BLUE, "一様な分布")
    ax.set_ylim(0, 5)
    ax.text(35, 3.7, "どの区間も\nほぼ同じ度数", ha="center", fontsize=10, color=GRAY)
    fig.tight_layout()
    fig.savefig(f"{OUT}/06_uniform.png", bbox_inches="tight")
    plt.close(fig)


# ── fig07: 右に裾が長い分布 ──────────────────────────────────
def fig07_right_skewed():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    bins = [0, 10, 20, 30, 40, 50, 60]
    counts = [10, 6, 3, 2, 1, 1]
    hist_chart(ax, bins, counts, "#f59e0b", "右に裾が長い分布", xlabel="値")
    ax.annotate("", xy=(55, 0.8), xytext=(25, 0.8),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.5))
    ax.text(42, 1.4, "裾が右に長い", fontsize=10, color=GRAY)
    ax.annotate("平均\n（中央値より右）", xy=(18, 3.5), xytext=(30, 7),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    fig.tight_layout()
    fig.savefig(f"{OUT}/07_right_skewed.png", bbox_inches="tight")
    plt.close(fig)


# ── fig08: 左に裾が長い分布 ──────────────────────────────────
def fig08_left_skewed():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    bins = [40, 50, 60, 70, 80, 90, 100]
    counts = [1, 1, 2, 3, 6, 10]
    hist_chart(ax, bins, counts, GREEN, "左に裾が長い分布", xlabel="値")
    ax.annotate("", xy=(45, 0.8), xytext=(68, 0.8),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.5))
    ax.text(52, 1.4, "裾が左に長い", fontsize=10, color=GRAY)
    ax.annotate("平均\n（中央値より左）", xy=(74, 3.5), xytext=(58, 7.5),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    fig.tight_layout()
    fig.savefig(f"{OUT}/08_left_skewed.png", bbox_inches="tight")
    plt.close(fig)


# ── fig09: 単峰と多峰 ─────────────────────────────────────────
def fig09_unimodal_bimodal():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

    ax = axes[0]
    bins = [40, 50, 60, 70, 80, 90]
    counts = [2, 5, 8, 5, 2]
    hist_chart(ax, bins, counts, BLUE, "単峰：山が1つ")
    ax.text(65, 8.7, "▲", ha="center", fontsize=14, color=BLUE)

    ax = axes[1]
    bins = [30, 40, 50, 60, 70, 80, 90]
    counts = [6, 5, 2, 2, 5, 6]
    hist_chart(ax, bins, counts, RED, "多峰：山が2つ\n（グループ混在の可能性）")
    ax.text(35, 6.7, "▲", ha="center", fontsize=14, color=RED)
    ax.text(85, 6.7, "▲", ha="center", fontsize=14, color=RED)

    fig.suptitle("単峰と多峰", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/09_unimodal_bimodal.png", bbox_inches="tight")
    plt.close(fig)


# ── fig10: 階級幅の違い ──────────────────────────────────────
def fig10_bin_width():
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

    ax = axes[0]
    bins_wide = [50, 70, 90, 100]
    counts_wide = [8, 10, 2]
    centers_wide = [60, 80, 95]
    widths_wide = [18, 18, 8]
    for c, h, w in zip(centers_wide, counts_wide, widths_wide):
        ax.bar(c, h, width=w * 0.9, color=BLUE, alpha=0.8, edgecolor="white", linewidth=1.5)
    ax.set_xticks([50, 70, 90, 100])
    ax.set_xlabel("点数", fontsize=11)
    ax.set_ylabel("人数", fontsize=11)
    ax.set_title("階級幅が広い（大ざっぱ）", fontsize=12, fontweight="bold")
    ax.set_ylim(0, 13)

    ax = axes[1]
    bins_narrow = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    counts_narrow = [1, 1, 2, 4, 3, 3, 2, 2, 1, 1]
    hist_chart(ax, bins_narrow, counts_narrow, BLUE, "階級幅が細かい（詳細）")

    fig.suptitle("同じデータでも階級幅で見え方が変わる", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/10_bin_width.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig01_bar_chart()
    fig02_histogram_basic()
    fig03_spread_comparison()
    fig04_symmetric()
    fig05_bell()
    fig06_uniform()
    fig07_right_skewed()
    fig08_left_skewed()
    fig09_unimodal_bimodal()
    fig10_bin_width()
    print("Done: data_types_lesson_assets/01〜10 を生成しました")
