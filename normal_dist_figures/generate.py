import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy import stats

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "assets"


def fig01_bell_curve():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    x = np.linspace(-4, 4, 400)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color="#2563eb", linewidth=2.5)
    ax.fill_between(x, y, alpha=0.1, color="#2563eb")
    ax.axvline(0, color="#6b7280", linewidth=1, linestyle="--")
    ax.set_xticks([0])
    ax.set_xticklabels(["平均 μ"], fontsize=12)
    ax.set_yticks([])
    ax.set_ylabel("確率密度", fontsize=11)
    ax.set_title("正規分布の基本形", fontsize=13, fontweight="bold")
    ax.annotate("平均付近が最も多い", xy=(0, stats.norm.pdf(0)),
                xytext=(1.2, 0.35), fontsize=10, color="#374151",
                arrowprops=dict(arrowstyle="->", color="#6b7280", lw=1))
    fig.tight_layout()
    fig.savefig(f"{OUT}/01_bell_curve.png", bbox_inches="tight")
    plt.close(fig)


def fig02_different_means():
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5), sharey=True)
    x50 = np.linspace(10, 90, 400)
    x70 = np.linspace(30, 110, 400)

    ax = axes[0]
    y = stats.norm.pdf(x50, loc=50, scale=10)
    ax.plot(x50, y, color="#2563eb", linewidth=2.5)
    ax.fill_between(x50, y, alpha=0.12, color="#2563eb")
    ax.axvline(50, color="#6b7280", linewidth=1, linestyle="--")
    ax.set_xticks([50])
    ax.set_xticklabels(["50"], fontsize=12)
    ax.set_yticks([])
    ax.set_title("平均 μ = 50", fontsize=12, fontweight="bold")
    ax.set_xlabel("X", fontsize=11)

    ax = axes[1]
    y = stats.norm.pdf(x70, loc=70, scale=10)
    ax.plot(x70, y, color="#dc2626", linewidth=2.5)
    ax.fill_between(x70, y, alpha=0.12, color="#dc2626")
    ax.axvline(70, color="#6b7280", linewidth=1, linestyle="--")
    ax.set_xticks([70])
    ax.set_xticklabels(["70"], fontsize=12)
    ax.set_yticks([])
    ax.set_title("平均 μ = 70（山が右へ移動）", fontsize=12, fontweight="bold")
    ax.set_xlabel("X", fontsize=11)

    fig.suptitle("平均が変わると山の位置が変わる", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/02_different_means.png", bbox_inches="tight")
    plt.close(fig)


def fig03_different_stds():
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5), sharey=False)
    x = np.linspace(-15, 15, 400)

    ax = axes[0]
    y = stats.norm.pdf(x, loc=0, scale=2)
    ax.plot(x, y, color="#2563eb", linewidth=2.5)
    ax.fill_between(x, y, alpha=0.12, color="#2563eb")
    ax.axvline(0, color="#6b7280", linewidth=1, linestyle="--")
    ax.set_xticks([0])
    ax.set_xticklabels(["μ"], fontsize=12)
    ax.set_yticks([])
    ax.set_title("標準偏差 σ が小さい\n（尖った・狭い）", fontsize=11, fontweight="bold")
    ax.set_xlabel("X", fontsize=11)
    ax.set_xlim(-12, 12)

    ax = axes[1]
    y = stats.norm.pdf(x, loc=0, scale=5)
    ax.plot(x, y, color="#dc2626", linewidth=2.5)
    ax.fill_between(x, y, alpha=0.12, color="#dc2626")
    ax.axvline(0, color="#6b7280", linewidth=1, linestyle="--")
    ax.set_xticks([0])
    ax.set_xticklabels(["μ"], fontsize=12)
    ax.set_yticks([])
    ax.set_title("標準偏差 σ が大きい\n（なだらか・広い）", fontsize=11, fontweight="bold")
    ax.set_xlabel("X", fontsize=11)
    ax.set_xlim(-12, 12)

    fig.suptitle("分散（標準偏差）が変わると広がりが変わる", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/03_different_stds.png", bbox_inches="tight")
    plt.close(fig)


def fig04_probability_as_area():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    x = np.linspace(10, 90, 400)
    mu, sigma = 50, 10
    y = stats.norm.pdf(x, loc=mu, scale=sigma)

    ax.plot(x, y, color="#2563eb", linewidth=2.5)

    x_fill = np.linspace(40, 60, 300)
    y_fill = stats.norm.pdf(x_fill, loc=mu, scale=sigma)
    ax.fill_between(x_fill, y_fill, alpha=0.4, color="#2563eb", label="P(40 ≦ X ≦ 60)")

    ax.axvline(40, color="#6b7280", linewidth=1, linestyle="--")
    ax.axvline(60, color="#6b7280", linewidth=1, linestyle="--")
    ax.axvline(50, color="#6b7280", linewidth=0.8, linestyle=":")

    prob = stats.norm.cdf(60, mu, sigma) - stats.norm.cdf(40, mu, sigma)
    ax.set_xticks([40, 50, 60])
    ax.set_xticklabels(["40", "μ=50", "60"], fontsize=11)
    ax.set_yticks([])
    ax.set_xlabel("X", fontsize=11)
    ax.set_ylabel("確率密度", fontsize=11)
    ax.set_title("確率は曲線下の面積", fontsize=13, fontweight="bold")

    ax.text(50, stats.norm.pdf(50, mu, sigma) * 0.45,
            f"面積 ≈ {prob:.1%}",
            ha="center", va="center", fontsize=12,
            color="white", fontweight="bold")

    ax.legend(fontsize=10, loc="upper right")
    fig.tight_layout()
    fig.savefig(f"{OUT}/04_probability_as_area.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig01_bell_curve()
    fig02_different_means()
    fig03_different_stds()
    fig04_probability_as_area()
    print("Done: assets/01〜04 を生成しました")
