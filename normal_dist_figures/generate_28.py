import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "../boxplot_lesson_assets"
BLUE = "#2563eb"
RED = "#dc2626"
GRAY = "#6b7280"
ORANGE = "#f59e0b"
GREEN = "#16a34a"


def fig01_quartile():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.annotate("", xy=(108, 0), xytext=(-8, 0),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=2))

    for x, label, pct, color in [
        (25, "Q1", "25%地点", BLUE),
        (50, "Q2\n（中央値）", "50%地点", RED),
        (75, "Q3", "75%地点", BLUE),
    ]:
        ax.plot([x, x], [-0.25, 0.25], color=color, lw=2.5)
        ax.text(x, 0.45, label, ha="center", va="bottom", fontsize=11,
                fontweight="bold", color=color)
        ax.text(x, -0.45, pct, ha="center", va="top", fontsize=9, color=GRAY)

    ax.text(-5, 0, "小さい値", ha="right", va="center", fontsize=10, color=GRAY)
    ax.text(105, 0, "大きい値", ha="left", va="center", fontsize=10, color=GRAY)
    ax.set_xlim(-15, 115)
    ax.set_ylim(-1.2, 1.3)
    ax.axis("off")
    ax.set_title("四分位数（Q1・Q2・Q3）の位置", fontsize=13, fontweight="bold", pad=10)
    fig.tight_layout()
    fig.savefig(f"{OUT}/28_01_quartile.png", bbox_inches="tight")
    plt.close(fig)


def fig02_iqr():
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.annotate("", xy=(108, 0), xytext=(-8, 0),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=2))

    ax.fill_betweenx([-0.3, 0.3], [25], [75], color=BLUE, alpha=0.18)

    for x, label, color in [(25, "Q1", BLUE), (75, "Q3", BLUE)]:
        ax.plot([x, x], [-0.3, 0.3], color=color, lw=2.5)
        ax.text(x, 0.5, label, ha="center", va="bottom", fontsize=12,
                fontweight="bold", color=color)

    ax.annotate("", xy=(75, -0.55), xytext=(25, -0.55),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2))
    ax.text(50, -0.9, "IQR = Q3 − Q1（中央50%の広がり）",
            ha="center", va="top", fontsize=10, color=BLUE, fontweight="bold")

    ax.text(-5, 0, "小さい値", ha="right", va="center", fontsize=10, color=GRAY)
    ax.text(105, 0, "大きい値", ha="left", va="center", fontsize=10, color=GRAY)
    ax.text(12, 0.05, "下位\n25%", ha="center", va="bottom", fontsize=8, color=GRAY)
    ax.text(50, 0.05, "中央50%", ha="center", va="bottom", fontsize=9, color=BLUE)
    ax.text(88, 0.05, "上位\n25%", ha="center", va="bottom", fontsize=8, color=GRAY)
    ax.set_xlim(-15, 115)
    ax.set_ylim(-1.4, 1.2)
    ax.axis("off")
    ax.set_title("四分位範囲（IQR）の意味", fontsize=13, fontweight="bold", pad=10)
    fig.tight_layout()
    fig.savefig(f"{OUT}/28_02_iqr.png", bbox_inches="tight")
    plt.close(fig)


def _style_bp(bp, box_color=BLUE, med_color=RED, whisk_color=GRAY):
    for b in bp["boxes"]:
        b.set_color(box_color); b.set_linewidth(2)
    for m in bp["medians"]:
        m.set_color(med_color); m.set_linewidth(2.5)
    for w in bp["whiskers"]:
        w.set_color(whisk_color); w.set_linewidth(1.8)
    for c in bp["caps"]:
        c.set_color(whisk_color); c.set_linewidth(1.8)
    for f in bp["fliers"]:
        f.set(marker="o", color=RED, alpha=0.7, markersize=8)


def fig03_boxplot_basic():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    data = [10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70]
    bp = ax.boxplot(data, vert=False, widths=0.35, patch_artist=False)
    _style_bp(bp)

    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    mn, mx = np.min(data), np.max(data)

    for x, label, color, dy in [
        (mn, "最小値", GRAY, 0.30),
        (q1, "Q1", BLUE, 0.37),
        (q3, "Q3", BLUE, 0.37),
        (mx, "最大値", GRAY, 0.30),
    ]:
        ax.annotate(label, xy=(x, 1), xytext=(x, 1 + dy),
                    ha="center", fontsize=10, color=color, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.2))

    ax.annotate("中央値（Q2）", xy=(q2, 1), xytext=(q2, 0.55),
                ha="center", fontsize=10, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.text((q1 + q3) / 2, 1.56, "← 箱（IQR）→",
            ha="center", fontsize=9, color=BLUE)
    ax.text((mn + q1) / 2, 0.62, "ひげ", ha="center", fontsize=9, color=GRAY)
    ax.text((q3 + mx) / 2, 0.62, "ひげ", ha="center", fontsize=9, color=GRAY)

    ax.set_ylim(0.3, 1.75)
    ax.set_yticks([])
    ax.set_xlabel("値", fontsize=11)
    ax.set_title("箱ひげ図の基本形（5数要約）", fontsize=13, fontweight="bold")
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/28_03_boxplot_basic.png", bbox_inches="tight")
    plt.close(fig)


def fig04_boxplot_median():
    fig, ax = plt.subplots(figsize=(7, 3.2))
    # 中央値がQ1寄り（右に裾が長いデータ）
    data = [5, 20, 21, 22, 60, 90]
    bp = ax.boxplot(data, vert=False, widths=0.35, patch_artist=False, whis=(0, 100))
    _style_bp(bp)

    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    ax.annotate("中央値はQ1寄り", xy=(q2, 1), xytext=(q2, 0.55),
                ha="center", fontsize=11, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.5))
    ax.annotate("Q1", xy=(q1, 1), xytext=(q1, 1.38),
                ha="center", fontsize=10, color=BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate("Q3", xy=(q3, 1), xytext=(q3, 1.38),
                ha="center", fontsize=10, color=BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))

    ax.set_ylim(0.3, 1.65)
    ax.set_yticks([])
    ax.set_xlabel("値", fontsize=11)
    ax.set_title("中央値は箱の中で必ずしも中央にあるわけではない\n（右裾が長いデータでは中央値がQ1寄りになる）",
                 fontsize=11, fontweight="bold")
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/28_04_boxplot_median.png", bbox_inches="tight")
    plt.close(fig)


def fig05_boxplot_skewed():
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

    ax = axes[0]
    data_r = [20, 25, 27, 28, 30, 32, 35, 38, 80, 100]
    bp = ax.boxplot(data_r, vert=False, widths=0.35, patch_artist=False, whis=(0, 100))
    _style_bp(bp, whisk_color=ORANGE)
    ax.annotate("右のひげが長い", xy=(90, 1), xytext=(65, 1.38),
                ha="center", fontsize=10, color=ORANGE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
    ax.set_title("右に裾が長い分布\n（大きい値の方向に広がる）", fontsize=11, fontweight="bold")
    ax.set_yticks([])
    ax.set_xlabel("値", fontsize=11)
    ax.spines["left"].set_visible(False)

    ax = axes[1]
    data_l = [0, 20, 65, 68, 70, 72, 75, 77, 78, 80]
    bp = ax.boxplot(data_l, vert=False, widths=0.35, patch_artist=False, whis=(0, 100))
    _style_bp(bp, whisk_color=GREEN)
    ax.annotate("左のひげが長い", xy=(10, 1), xytext=(35, 1.38),
                ha="center", fontsize=10, color=GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.set_title("左に裾が長い分布\n（小さい値の方向に広がる）", fontsize=11, fontweight="bold")
    ax.set_yticks([])
    ax.set_xlabel("値", fontsize=11)
    ax.spines["left"].set_visible(False)

    fig.suptitle("箱ひげ図で分布の歪みを読む", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/28_05_boxplot_skewed.png", bbox_inches="tight")
    plt.close(fig)


def fig06_boxplot_compare():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    data_a = [60, 63, 65, 67, 70, 73, 75, 77, 80]
    data_b = [55, 58, 62, 63, 65, 68, 80, 95, 100, 110]
    bp = ax.boxplot([data_a, data_b], vert=False, widths=0.4, patch_artist=False)

    colors = [BLUE, RED]
    whisk_colors = [GRAY, ORANGE]
    for i in range(2):
        bp["boxes"][i].set_color(colors[i]); bp["boxes"][i].set_linewidth(2)
        bp["medians"][i].set_color(colors[i]); bp["medians"][i].set_linewidth(2.5)
        for j in range(2):
            bp["whiskers"][2*i+j].set_color(whisk_colors[i])
            bp["whiskers"][2*i+j].set_linewidth(1.8)
            bp["caps"][2*i+j].set_color(whisk_colors[i])
            bp["caps"][2*i+j].set_linewidth(1.8)

    ax.set_yticklabels(["A校", "B校"], fontsize=13)
    ax.set_xlabel("テスト点数", fontsize=11)
    ax.set_title("A校 vs B校：箱ひげ図による比較", fontsize=13, fontweight="bold")

    med_a = np.median(data_a)
    med_b = np.median(data_b)
    ax.text(med_a, 1.38, f"A校の中央値\n{med_a:.0f}点", ha="center", fontsize=9, color=BLUE)
    ax.text(med_b, 1.62, f"B校の中央値\n{med_b:.1f}点", ha="center", fontsize=9, color=RED)

    fig.tight_layout()
    fig.savefig(f"{OUT}/28_06_boxplot_compare.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig01_quartile()
    fig02_iqr()
    fig03_boxplot_basic()
    fig04_boxplot_median()
    fig05_boxplot_skewed()
    fig06_boxplot_compare()
    print("Done: boxplot_lesson_assets/28_01〜06 を生成しました")
