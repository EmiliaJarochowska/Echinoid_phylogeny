from skbio import DistanceMatrix
from skbio.sequence.distance import hamming
from skbio.tree import nj
import pandas as pd
import numpy as np

# Read in a distance matrix in Excel

df = pd.read_excel(r"matrix.xlsx")

Taxa = df.iloc[:, 0]
Characters = df.iloc[:, 1:]

# To create a Sequence object, we need to change the type of the character values recognized by pandas
sequences_str = Characters.values.astype(np.uint8)

# Create a list of objects of the type Sequence (speficif to scikit-bio)
sequences = [Sequence(seq) for seq in sequences_str]

# Calculate pairwise distances using Hamming distance
num_sequences = len(sequences)
distances = np.zeros((num_sequences, num_sequences))
for i in range(num_sequences):
    for j in range(i, num_sequences):
        distance = hamming(sequences[i], sequences[j])
        distances[i, j] = distance
        distances[j, i] = distance

# Convert the pairwise distances into scikit-bio's distance matrix object
distance_matrix = DistanceMatrix(distances, ids=Taxa)

# Check how it looks
print(distance_matrix)

# Create a tree using the neighbor-joining algorithm
tree = nj(distance_matrix)

# Export the tree into the Newick format that can be read by various programs
newick_string = tree.write("tree.newick")