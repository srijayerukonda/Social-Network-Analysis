# Social Network Analysis Using Centrality Metrics

## 1. Project Overview
This project analyses a social network using graph theory and Social Network Analysis (SNA) techniques. It identifies important nodes based on their connections, influence, and positions within the network.

## 2. Objectives
- Analyse the structure of a social network.
- Calculate Degree, Closeness, Betweenness, and Eigenvector Centrality.
- Identify the top-ranked nodes for each centrality metric.
- Study correlations between centrality metrics.
- Visualise the network and centrality results.

## 3. Dataset
The project uses the built-in Karate Club social network dataset provided by NetworkX.

- Nodes: 34
- Edges: 78
- Network type: Undirected graph

## 4. Technologies Used
- Python
- Jupyter Notebook
- NetworkX
- Pandas
- Matplotlib
- Seaborn

## 5. Centrality Metrics
- **Degree Centrality:** Measures the number of direct connections relative to the maximum possible connections.
- **Closeness Centrality:** Measures how close a node is to other nodes based on shortest paths.
- **Betweenness Centrality:** Measures how frequently a node lies on shortest paths between other nodes.
- **Eigenvector Centrality:** Measures a node's importance based on its connections to other important nodes.

## 6. Project Structure
- main.ipynb: Main analysis and results.
- centrality_analysis.py: Centrality calculations, rankings, and correlations.
- visualization.py: Network and chart visualisation functions.
- data/: Dataset folder.
- results/: Exported CSV files and visualisations.
- requirements.txt: Required Python libraries.

## 7. How to Run
1. Install Python and Jupyter Notebook.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Open main.ipynb in Jupyter Notebook.
4. Run the notebook cells in order.

## 8. Outputs
The results folder contains:
- Centrality scores for all nodes.
- Correlation matrix for the four centrality metrics.
- Combined node rankings.
- Social network graph.
- Centrality bar charts.
- Centrality correlation heatmap.
- Centrality distribution chart.

## 9. Conclusion
This project demonstrates how centrality metrics can be used to identify structurally important nodes in a social network. Comparing multiple metrics provides different perspectives on connectivity, information flow, and node influence.
