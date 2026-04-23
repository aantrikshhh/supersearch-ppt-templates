"""Generate category-specific knowledge graph PNG images for slide 11.

Each image shows a shopper query decomposed through a knowledge context graph
into intent nodes, keyword nodes, and final product results.

Visual style matches the existing template: rounded rectangles with thin black
borders, downward arrows, light blue result nodes, subtle grid background.
"""

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


GRAPHS_DIR = Path(__file__).parent / "graphs"

NODE_FACE = "#FFFFFF"
NODE_EDGE = "#444444"
RESULT_FACE = "#D6E4F0"
RESULT_EDGE = "#444444"
ARROW_COLOR = "#444444"
BG_COLOR = "#FFFFFF"
GRID_COLOR = "#E8E8E8"
TEXT_COLOR = "#333333"

FIG_W, FIG_H = 12.0, 5.5
DPI = 150


def _draw_node(ax, cx, cy, text, w=1.4, h=0.38, is_result=False, fontsize=8):
    face = RESULT_FACE if is_result else NODE_FACE
    edge = RESULT_EDGE if is_result else NODE_EDGE
    box = FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.05",
        facecolor=face, edgecolor=edge, linewidth=1.0,
        zorder=3,
    )
    ax.add_patch(box)
    ax.text(
        cx, cy, text,
        ha="center", va="center",
        fontsize=fontsize, color=TEXT_COLOR,
        zorder=4, wrap=True,
        fontfamily="sans-serif",
    )
    return cx, cy, w, h


def _draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2 + 0.19), xytext=(x1, y1 - 0.19),
        arrowprops=dict(
            arrowstyle="-|>",
            color=ARROW_COLOR,
            linewidth=1.0,
            shrinkA=0, shrinkB=0,
        ),
        zorder=2,
    )


def generate_graph(graph_def, output_path):
    """Generate a knowledge graph PNG from a graph definition dict.

    graph_def keys:
        query: str — the root shopper query
        intents: list of str — level-2 intent nodes
        keywords: dict mapping intent -> list of keyword strings — level-3
        sub_keywords: dict mapping keyword -> list of sub-keyword strings — level-4 (optional)
        results: list of str — bottom result nodes
    """
    query = graph_def["query"]
    intents = graph_def["intents"]
    keywords = graph_def["keywords"]
    sub_keywords = graph_def.get("sub_keywords", {})
    results = graph_def["results"]

    fig, ax = plt.subplots(1, 1, figsize=(FIG_W, FIG_H), dpi=DPI)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    for x in range(0, 13):
        ax.axvline(x, color=GRID_COLOR, linewidth=0.3, zorder=0)
    for y_val in [v * 0.5 for v in range(0, 12)]:
        ax.axhline(y_val, color=GRID_COLOR, linewidth=0.3, zorder=0)

    y_query = 5.0
    y_intent = 3.9
    y_keyword = 2.8
    y_subkw = 1.7
    y_result = 0.5

    has_sub = bool(sub_keywords)
    if not has_sub:
        y_keyword = 3.0
        y_result = 1.2

    center_x = 5.5
    _draw_node(ax, center_x, y_query, query, w=3.2, h=0.5, fontsize=8.5)

    n_intents = len(intents)
    intent_spread = min(3.5, 1.8 * n_intents)
    intent_xs = []
    for i, intent in enumerate(intents):
        if n_intents == 1:
            ix = center_x
        else:
            ix = center_x - intent_spread + (2 * intent_spread * i / (n_intents - 1))
        intent_xs.append(ix)
        _draw_node(ax, ix, y_intent, intent, w=1.4, h=0.38)
        _draw_arrow(ax, center_x, y_query, ix, y_intent)

    all_kw_positions = []
    total_kws = sum(len(keywords.get(intent, [])) for intent in intents)
    if total_kws == 0:
        total_kws = 1
    total_spread = min(10.0, 1.5 * total_kws)
    kw_start_x = center_x - total_spread / 2

    kw_idx = 0
    for i, intent in enumerate(intents):
        kws = keywords.get(intent, [])
        for kw in kws:
            if total_kws == 1:
                kx = center_x
            else:
                kx = kw_start_x + (total_spread * kw_idx / (total_kws - 1))
            _draw_node(ax, kx, y_keyword, kw, w=1.3, h=0.38, fontsize=7.5)
            _draw_arrow(ax, intent_xs[i], y_intent, kx, y_keyword)
            all_kw_positions.append((kw, kx))
            kw_idx += 1

    if has_sub:
        sub_positions = []
        all_subs = []
        for kw, kx in all_kw_positions:
            subs = sub_keywords.get(kw, [])
            all_subs.extend([(s, kx) for s in subs])

        if all_subs:
            n_subs = len(all_subs)
            sub_spread = min(6.0, 1.5 * n_subs)
            sub_start = center_x - sub_spread / 2
            for si, (sub_text, parent_kx) in enumerate(all_subs):
                if n_subs == 1:
                    sx = center_x
                else:
                    sx = sub_start + (sub_spread * si / (n_subs - 1))
                _draw_node(ax, sx, y_subkw, sub_text, w=1.2, h=0.38, fontsize=7.5)
                _draw_arrow(ax, parent_kx, y_keyword, sx, y_subkw)

    n_results = len(results)
    result_spread = min(10.0, 2.0 * n_results)
    result_start = center_x - result_spread / 2
    for ri, result_text in enumerate(results):
        if n_results == 1:
            rx = center_x
        else:
            rx = result_start + (result_spread * ri / (n_results - 1))
        _draw_node(ax, rx, y_result, result_text, w=1.8, h=0.45,
                   is_result=True, fontsize=7)

    plt.tight_layout(pad=0.3)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight",
                facecolor=BG_COLOR, edgecolor="none")
    plt.close(fig)
    print(f"  Generated {output_path}")


def generate_all(graph_definitions):
    for category, gdef in graph_definitions.items():
        out = GRAPHS_DIR / f"{category}_graph.png"
        generate_graph(gdef, out)


if __name__ == "__main__":
    from category_content import CATEGORIES
    defs = {k: v["graph_definition"] for k, v in CATEGORIES.items()}
    generate_all(defs)
