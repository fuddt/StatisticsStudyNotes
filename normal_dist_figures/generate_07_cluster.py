import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

plt.rcParams.update({
    "font.family": ["Hiragino Sans", "YuGothic", "AppleGothic", "sans-serif"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

OUT = "../cluster_lesson_assets"
BLUE = "#2563eb"
RED = "#dc2626"
GRAY = "#6b7280"
ORANGE = "#f59e0b"
GREEN = "#16a34a"
PURPLE = "#7c3aed"


def fig01_cluster_scatter():
    """3 natural clusters in market state space"""
    rng = np.random.default_rng(42)

    c0 = rng.normal([0.12, 0.18], 0.04, (5, 2))  # 通常市場
    c1 = rng.normal([0.48, 0.48], 0.05, (5, 2))  # 中程度の歪み市場
    c2 = rng.normal([0.83, 0.83], 0.04, (5, 2))  # 強い歪み市場

    fig, ax = plt.subplots(figsize=(7, 5))

    for data, color, label in [
        (c0, BLUE,   "通常市場（左下）"),
        (c1, ORANGE, "中程度の歪み市場（中央）"),
        (c2, RED,    "強い歪み市場（右上）"),
    ]:
        ax.scatter(data[:, 0], data[:, 1], color=color, s=130, alpha=0.88,
                   edgecolors="white", lw=0.8, zorder=3, label=label)

    ax.set_xlabel("市場集中度", fontsize=12)
    ax.set_ylabel("馬券種間歪み", fontsize=12)
    ax.set_title("市場状態の3クラスター（散布図）", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_xlim(-0.05, 1.1)
    ax.set_ylim(-0.05, 1.1)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUT}/07_01_cluster_scatter.png", bbox_inches="tight")
    plt.close(fig)


def fig02_distance_concept():
    """A, B, C points showing near/far distance"""
    fig, ax = plt.subplots(figsize=(6, 4.5))

    points = {
        "A": (1.0, 1.5),
        "B": (2.5, 3.0),
        "C": (5.5, 6.0),
    }

    for name, (x, y) in points.items():
        color = RED if name == "C" else BLUE
        ax.scatter(x, y, s=200, color=color, edgecolors="white", lw=1, zorder=4)
        ax.text(x + 0.18, y + 0.18, name, fontsize=14, fontweight="bold", color=color)

    ax.annotate("", xy=points["B"], xytext=points["A"],
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2))
    ax.text(1.75, 2.0, "近い", ha="center", fontsize=11, color=BLUE, fontweight="bold")

    ax.annotate("", xy=points["C"], xytext=points["A"],
                arrowprops=dict(arrowstyle="<->", color=RED, lw=2))
    ax.text(2.8, 4.5, "遠い", ha="center", fontsize=11, color=RED, fontweight="bold")

    ax.set_xlabel("x（特徴量1）", fontsize=11)
    ax.set_ylabel("y（特徴量2）", fontsize=11)
    ax.set_title("データ間の距離の直感\nAとBは近い → 同じグループになりやすい", fontsize=12, fontweight="bold")
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7.5)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUT}/07_02_distance_concept.png", bbox_inches="tight")
    plt.close(fig)


def fig03_dendrogram():
    """Dendrogram of 6 'races' A-F"""
    data = np.array([
        [0.10, 0.20],  # A
        [0.15, 0.25],  # B
        [0.80, 0.75],  # C
        [0.85, 0.78],  # D
        [0.40, 0.90],  # E
        [0.45, 0.88],  # F
    ])

    fig, ax = plt.subplots(figsize=(8, 5))

    Z = sch.linkage(data, method="ward")
    sch.dendrogram(
        Z,
        labels=["A", "B", "C", "D", "E", "F"],
        ax=ax,
        color_threshold=0.4,
        above_threshold_color=GRAY,
        link_color_func=lambda k: [BLUE, BLUE, RED, RED, ORANGE, ORANGE, GREEN][min(k, 6)],
    )

    ax.set_xlabel("レース", fontsize=12)
    ax.set_ylabel("距離（非類似度）", fontsize=12)
    ax.set_title("デンドログラム：近いもの同士が順番に結合する\n（低い位置で結合 = より似ている）",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(f"{OUT}/07_03_dendrogram.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    fig01_cluster_scatter()
    fig02_distance_concept()
    fig03_dendrogram()
    print("Done: cluster_lesson_assets/07_01〜03 を生成しました")
