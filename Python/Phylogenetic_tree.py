from skbio import DistanceMatrix
from skbio.tree import nj
import pandas as pd
import numpy as np

# Read in a distance matrix in Excel

df = pd.read_excel(r"matrix.xlsx")

Taxa = df.iloc[:, 0]
Characters = df.iloc[:, 1:]

# We need to change the type of the character values recognized by pandas
sequences_str = Characters.values.astype(np.uint8)

# Function calculating Euclidean distance from a character matrix
def euclidean(matrix):
    squared_dist = np.square(matrix[:, np.newaxis] - matrix).sum(axis=2)
    distances = np.sqrt(squared_dist)
    return distances

# Calculate distances for your character matrix
distances = euclidean(sequences_str)

# Convert the pairwise distances into scikit-bio's distance matrix object
distance_matrix = DistanceMatrix(distances, ids=Taxa)

# Check how it looks
print(distance_matrix)

# Create a tree using the neighbor-joining algorithm
tree = nj(distance_matrix)

# Export the tree into the Newick format that can be read by various programs
newick_string = tree.write("tree.newick")