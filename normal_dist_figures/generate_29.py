import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "../dispersion_lesson_assets"
BLUE = "#2563eb"
RED = "#dc2626"
GRAY = "#6b7280"
ORANGE = "#f59e0b"
GREEN = "#16a34a"


def hist_bar(ax, bins, counts, color, title, xlabel="値", ylabel="度数"):
    w = bins[1] - bins[0]
    centers = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]
    ax.bar(centers, counts, width=w * 0.9, color=color, alpha=0.85,
           edgecolor="white", linewidth=1.5)
    ax.set_xticks(bins)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_ylim(0, max(counts) * 1.3)


def fig01_skewness():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

    ax = axes[0]
    bins = [0, 10, 20, 30, 40, 50, 60]
    counts = [10, 6, 3, 2, 1, 1]
    hist_bar(ax, bins, counts, ORANGE, "歪度 > 0（正の歪度）\n右に裾が長い")
    ax.text(38, 8.5, "平均 > 中央値", ha="center", fontsize=9, color=RED, fontweight="bold")
    ax.annotate("", xy=(50, 1), xytext=(25, 1),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.5))
    ax.text(38, 1.8, "裾が右へ長い", ha="center", fontsize=8, color=GRAY)

    ax = axes[1]
    bins = [40, 50, 60, 70, 80, 90, 100]
    counts = [1, 1, 2, 3, 6, 10]
    hist_bar(ax, bins, counts, GREEN, "歪度 < 0（負の歪度）\n左に裾が長い")
    ax.text(62, 8.5, "平均 < 中央値", ha="center", fontsize=9, color=RED, fontweight="bold")
    ax.annotate("", xy=(50, 1), xytext=(75, 1),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.5))
    ax.text(62, 1.8, "裾が左へ長い", ha="center", fontsize=8, color=GRAY)

    fig.suptitle("歪度：分布の左右非対称性", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/29_01_skewness.png", bbox_inches="tight")
    plt.close(fig)


def fig02_kurtosis():
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.linspace(-5, 5, 400)

    y_normal = stats.norm.pdf(x)
    ax.plot(x, y_normal, color=BLUE, lw=2.5, label="正規分布（基準の尖度）", zorder=3)
    ax.fill_between(x, y_normal, alpha=0.12, color=BLUE)

    # Laplace is leptokurtic (excess kurtosis=3): tall peak, heavy tails
    y_lept = stats.laplace.pdf(x, scale=0.7)
    ax.plot(x, y_lept, color=RED, lw=2.5,
            label="尖度が大きい分布\n（中央に集まるが裾が厚い）", zorder=2)
    ax.fill_between(x, y_lept, alpha=0.1, color=RED)

    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_ylabel("確率密度", fontsize=11)
    ax.set_xlabel("値", fontsize=11)
    ax.set_title("尖度の違い：中央の高さと裾の厚さ", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10, loc="upper right")

    ax.annotate("中央が高い", xy=(0, stats.laplace.pdf(0, scale=0.7)),
                xytext=(1.5, 0.57), fontsize=9, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1))
    ax.annotate("裾が厚い\n（極端な値が出やすい）",
                xy=(2.5, stats.laplace.pdf(2.5, scale=0.7)),
                xytext=(2.3, 0.2), fontsize=9, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1))

    fig.tight_layout()
    fig.savefig(f"{OUT}/29_02_kurtosis.png", bbox_inches="tight")
    plt.close(fig)


def fig03_lorenz():
    fig, ax = plt.subplots(figsize=(6, 5.5))

    x = [0, 20, 40, 60, 80, 100]
    y_equal = [0, 20, 40, 60, 80, 100]
    y_lorenz = [0, 5, 15, 30, 55, 100]

    ax.plot(x, y_equal, color=BLUE, lw=2.5, ls="--", label="完全平等線（45°直線）")
    ax.plot(x, y_lorenz, color=RED, lw=2.5, marker="o", markersize=7,
            label="ローレンツ曲線（格差あり）")
    ax.fill_between(x, y_lorenz, y_equal, alpha=0.18, color=RED,
                    label="ジニ係数に対応する面積")

    ax.set_xlabel("人口の累積割合（%）", fontsize=11)
    ax.set_ylabel("所得の累積割合（%）", fontsize=11)
    ax.set_title("ローレンツ曲線とジニ係数", fontsize=13, fontweight="bold")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.text(60, 22, "ジニ係数 ∝ この面積\n（大きいほど格差が大きい）",
            ha="center", fontsize=9, color=RED)

    fig.tight_layout()
    fig.savefig(f"{OUT}/29_03_lorenz.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig01_skewness()
    fig02_kurtosis()
    fig03_lorenz()
    print("Done: dispersion_lesson_assets/29_01〜03 を生成しました")
