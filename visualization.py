
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def plot_network(G, scores=None, title="Social Network"):
    """
    Draw a social network.
    If scores are provided, node colors represent centrality.
    """

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))

    if scores is None:
        node_colors = "skyblue"
        color_map = None
    else:
        node_colors = [scores[n] for n in G.nodes()]
        color_map = plt.cm.viridis

    nx.draw_networkx(
        G,
        pos=pos,
        node_color=node_colors,
        cmap=color_map,
        node_size=600,
        edge_color="gray",
        font_size=9,
        with_labels=True
    )

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def plot_top_nodes(results, metric, top_n=10):
    """
    Display a bar chart of the top-ranked nodes
    for the selected centrality metric.
    """

    top_nodes = results.nlargest(top_n, metric)

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=top_nodes,
        x="Node",
        y=metric
    )

    plt.title(f"Top {top_n} Nodes by {metric}")
    plt.xlabel("Node ID")
    plt.ylabel(metric)
    plt.tight_layout()
    plt.show()


def plot_metric_distributions(results):
    """
    Compare the score distributions of all four metrics.
    """

    metrics = [
        "Degree Centrality",
        "Closeness Centrality",
        "Betweenness Centrality",
        "Eigenvector Centrality"
    ]

    long_data = results.melt(
        id_vars="Node",
        value_vars=metrics,
        var_name="Centrality Metric",
        value_name="Score"
    )

    plt.figure(figsize=(12, 6))

    sns.boxplot(
        data=long_data,
        x="Centrality Metric",
        y="Score"
    )

    plt.title("Distribution of Centrality Metrics")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()
