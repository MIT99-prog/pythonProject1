# -------------------------------------------------------------------------------
# Name:        cluster
# Purpose:     to test functions of Cluster of Scikit-learn
#
# Author:      tango
#
# Created:     26/10/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from matplotlib import pyplot as plt
from pandas import plotting  # 高度なプロットを行うツールのインポート
from scipy.cluster.hierarchy import linkage, dendrogram


class Cluster:
    def __init__(self):
        pass

    def check_data(self, st):
        # Check data contents
        plotting.scatter_matrix(st.df[st.df.columns[0:5]], figsize=(8, 8), alpha=0.8, diagonal='kde')  # 全体像を眺める
        plt.show()
    """
        # Define Data
        self.x = st.df.loc[:, ['Open', 'Close', 'High', 'Low']].values



        # setting distance_threshold=0 ensures we compute the full tree.
        model = AgglomerativeClustering(affinity='euclidean',
                                        linkage='ward',
                                        distance_threshold=0,
                                        n_clusters=None)

        self.model = model.fit(self.x)

        # self.disply_graph()
        
    def plot_dendrogram(self, **kwargs):
        # Create linkage matrix and then plot the dendrogram

        # create the counts of samples under each node
        counts = np.zeros(self.model.children_.shape[0])
        n_samples = len(self.model.labels_)
        for i, merge in enumerate(self.model.children_):
            current_count = 0
            for child_idx in merge:
                if child_idx < n_samples:
                    current_count += 1  # leaf node
                else:
                    current_count += counts[child_idx - n_samples]
            counts[i] = current_count

        linkage_matrix = np.column_stack([self.model.children_, self.model.distances_,
                                          counts]).astype(float)

        # Plot the corresponding dendrogram
        dendrogram(linkage_matrix, **kwargs)
    """
    def disply_graph(self, st, metric, method):
        # Exec Analysis
        result1 = linkage(st.df.iloc[:, 0:5], metric=metric, method=method)
        # Generate dendrogram
        dendrogram(result1)
        plt.title('Dendrogram ' + metric + ' / ' + method)
        plt.ylabel("Threshold")
        plt.show()
