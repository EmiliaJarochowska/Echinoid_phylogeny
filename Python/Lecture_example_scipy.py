import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

df0 = pd.read_excel(r"Python/Lecture_example.xlsx") # turn .xlsx file into data frame
df = df0.T

Taxa = df.index.tolist()[1:] # select taxon names
Characters = df.iloc[1:, :] # select character vaues

# We need to change the type of the character values recognized by pandas
sequences_str = Characters.values.astype(np.uint8)

# Calculate distance matrix
distance_matrix = squareform(pdist(sequences_str, metric='euclidean'))

# Visualization distance matrix
fig, ax = plt.subplots()
cax = ax.matshow(distance_matrix, cmap='viridis')

# Distance values for matrix cells
for i in range(len(sequences_str)):
    for j in range(len(len(sequences_str))):
        ax.text(j, i, f'{distance_matrix[i, j]:.2f}', ha='center', va='center', color='white')

# Add color bar
cbar = fig.colorbar(cax)
cbar.ax.set_ylabel('Distance', rotation=270, labelpad=15)

# Show chart
plt.title('Distance Matrix')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.show()

Z = linkage(pdist(sequences_str, metric='euclidean'), method='weighted')

plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Hierarchical Cluster Dendrogram')
plt.xlabel('Data Point Indexes')
plt.ylabel('Distance')
plt.show()