import numpy as np

def silhouette_score(X: list, labels: list[int]) -> float:

    X = np.array(X, dtype=float)
    labels = np.array(labels)

    score = []

    for i in range(len(X)):

        current_label = labels[i]

        # Distance from current point to every point
        distances = np.linalg.norm(X - X[i], axis=1)

        # Points belonging to current cluster
        same_cluster = labels == current_label

        # Remove the current point itself
        own_indices = np.where(same_cluster)[0]
        own_indices = own_indices[own_indices != i]

        # a(i)
        a = np.mean(distances[own_indices])

        # Find all other cluster labels
        other_labels = np.unique(labels[labels != current_label])

        cluster_distances = []

        for label in other_labels:

            # Points belonging to this particular other cluster
            other_clusters = labels == label

            # Average distance to this cluster
            avg_distance = np.mean(distances[other_clusters])

            cluster_distances.append(avg_distance)

        # b(i)
        b = min(cluster_distances)

        # silhouette
        s = (b - a) / max(a, b)

        score.append(s)

    return float(np.mean(score))