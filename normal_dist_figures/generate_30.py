import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "../scatter_lesson_assets"
BLUE = "#2563eb"
RED = "#dc2626"
GRAY = "#6b7280"
ORANGE = "#f59e0b"
GREEN = "#16a34a"
PURPLE = "#7c3aed"


def correlated(r, n=25, seed=0):
    rng = np.random.default_rng(seed)
    x = rng.normal(0, 1, n)
    noise = rng.normal(0, np.sqrt(max(1e-9, 1 - r**2)), n)
    y = r * x + noise
    return x, y


def trend_line(ax, x, y, color):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    xs = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, p(xs), color=color, lw=1.5, ls="--", alpha=0.55)


def fig01_scatter_intro():
    fig, ax = plt.subplots(figsize=(6, 4))
    hours = [1, 2, 3, 4, 5, 5, 6]
    scores = [40, 50, 60, 60, 70, 80, 80]
    ax.scatter(hours, scores, color=BLUE, s=110, alpha=0.85,
               edgecolors="white", lw=0.5, zorder=3)
    z = np.polyfit(hours, scores, 1)
    xs = np.linspace(0.5, 6.5, 100)
    ax.plot(xs, np.poly1d(z)(xs), color=RED, lw=1.8, ls="--", alpha=0.65, label="傾向線")
    ax.set_xlabel("勉強時間（時間）", fontsize=12)
    ax.set_ylabel("テスト点数（点）", fontsize=12)
    ax.set_title("勉強時間とテスト点数の散布図", fontsize=13, fontweight="bold")
    ax.set_xlim(0, 7)
    ax.set_ylim(30, 95)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUT}/30_01_scatter_intro.png", bbox_inches="tight")
    plt.close(fig)


def fig02_scatter_types():
    fig, axes = plt.subplots(2, 2, figsize=(9, 7))
    rng = np.random.default_rng(42)

    # 正の関係
    ax = axes[0, 0]
    x, y = correlated(0.9, seed=1)
    ax.scatter(x, y, color=BLUE, s=55, alpha=0.8, edgecolors="white", lw=0.5)
    trend_line(ax, x, y, BLUE)
    ax.set_title("正の関係\n（一方が増えるともう一方も増える）", fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])

    # 負の関係
    ax = axes[0, 1]
    x, y = correlated(-0.9, seed=2)
    ax.scatter(x, y, color=RED, s=55, alpha=0.8, edgecolors="white", lw=0.5)
    trend_line(ax, x, y, RED)
    ax.set_title("負の関係\n（一方が増えるともう一方は減る）", fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])

    # 関係なし
    ax = axes[1, 0]
    x, y = correlated(0.0, seed=3)
    ax.scatter(x, y, color=GRAY, s=55, alpha=0.8, edgecolors="white", lw=0.5)
    ax.set_title("関係がなさそう\n（直線的な傾向が見えない）", fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])

    # U字型（非線形）
    ax = axes[1, 1]
    x_u = np.linspace(-2, 2, 20)
    y_u = x_u**2 + rng.normal(0, 0.25, 20)
    ax.scatter(x_u, y_u, color=ORANGE, s=55, alpha=0.8, edgecolors="white", lw=0.5)
    ax.set_title("U字型（非線形）\n（相関係数では捉えられない関係）",
                 fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])

    fig.suptitle("散布図で見られる関係のパターン", fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()
    fig.savefig(f"{OUT}/30_02_scatter_types.png", bbox_inches="tight")
    plt.close(fig)


def fig03_scatter_strength():
    fig, axes = plt.subplots(2, 2, figsize=(9, 7))

    configs = [
        (0.95, BLUE,   "強い正の相関", axes[0, 0], 1),
        (0.25, BLUE,   "弱い正の相関", axes[0, 1], 2),
        (-0.90, RED,   "強い負の相関", axes[1, 0], 3),
        (0.02, GRAY,   "相関ほぼゼロ", axes[1, 1], 4),
    ]

    for r, color, title, ax, seed in configs:
        x, y = correlated(r, n=30, seed=seed)
        ax.scatter(x, y, color=color, s=55, alpha=0.8, edgecolors="white", lw=0.5)
        if abs(r) > 0.1:
            trend_line(ax, x, y, color)
        ax.set_title(f"{title}\n（r = {r:.2f}）", fontsize=11, fontweight="bold")
        ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])

    fig.suptitle("相関係数の強さと散布図の形", fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()
    fig.savefig(f"{OUT}/30_03_scatter_strength.png", bbox_inches="tight")
    plt.close(fig)


def fig04_scatter_outlier():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    rng = np.random.default_rng(42)
    x_base = rng.uniform(0, 5, 15)
    y_base = rng.uniform(0, 5, 15)

    # Without outlier
    ax = axes[0]
    ax.scatter(x_base, y_base, color=BLUE, s=75, alpha=0.8, edgecolors="white", lw=0.5)
    r_no = np.corrcoef(x_base, y_base)[0, 1]
    ax.set_title(f"外れ値なし\n（r ≈ {r_no:.2f}：ほぼ無相関）", fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(-0.5, 12); ax.set_ylim(-0.5, 12)

    # With outlier
    ax = axes[1]
    x_out, y_out = np.append(x_base, 10), np.append(y_base, 10)
    ax.scatter(x_base, y_base, color=BLUE, s=75, alpha=0.8, edgecolors="white", lw=0.5)
    ax.scatter([10], [10], color=RED, s=160, alpha=1, edgecolors="white", lw=1,
               zorder=5, label="外れ値（1点）")
    ax.annotate("この1点が\n相関を作る", xy=(10, 10), xytext=(6.5, 8),
                fontsize=9, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    z = np.polyfit(x_out, y_out, 1)
    xs = np.linspace(-0.5, 11, 100)
    r_with = np.corrcoef(x_out, y_out)[0, 1]
    ax.plot(xs, np.poly1d(z)(xs), color=RED, lw=1.8, ls="--", alpha=0.65,
            label=f"傾向線（r ≈ {r_with:.2f}）")
    ax.set_title(f"外れ値あり\n（r ≈ {r_with:.2f}：見かけの相関が生じる）",
                 fontsize=11, fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(-0.5, 12); ax.set_ylim(-0.5, 12)
    ax.legend(fontsize=9, loc="lower right")

    fig.suptitle("外れ値が相関係数に与える影響", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(f"{OUT}/30_04_scatter_outlier.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig01_scatter_intro()
    fig02_scatter_types()
    fig03_scatter_strength()
    fig04_scatter_outlier()
    print("Done: scatter_lesson_assets/30_01〜04 を生成しました")
