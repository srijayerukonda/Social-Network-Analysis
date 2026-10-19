
import networkx as nx
import pandas as pd


def calculate_centrality(G):
    """
    Calculate four centrality measures for every node
    in the given social network.
    """

    degree = nx.degree_centrality(G)
    closeness = nx.closeness_centrality(G)

    betweenness = nx.betweenness_centrality(
        G,
        normalized=True
    )

    eigenvector = nx.eigenvector_centrality(
        G,
        max_iter=1000
    )

    results = pd.DataFrame({
        "Node": list(G.nodes()),
        "Degree Centrality": [
            degree[n] for n in G.nodes()
        ],
        "Closeness Centrality": [
            closeness[n] for n in G.nodes()
        ],
        "Betweenness Centrality": [
            betweenness[n] for n in G.nodes()
        ],
        "Eigenvector Centrality": [
            eigenvector[n] for n in G.nodes()
        ]
    })

    return results


def rank_nodes(results, metric, top_n=5):
    """
    Return the highest-ranked nodes for a given metric.
    """

    if metric not in results.columns:
        raise ValueError(
            f"Unknown metric: {metric}"
        )

    return (
        results[["Node", metric]]
        .sort_values(
            by=metric,
            ascending=False
        )
        .head(top_n)
        .reset_index(drop=True)
    )


def calculate_metric_correlations(results):
    """
    Calculate correlations between centrality measures.
    """

    metrics = [
        "Degree Centrality",
        "Closeness Centrality",
        "Betweenness Centrality",
        "Eigenvector Centrality"
    ]

    return results[metrics].corr()
