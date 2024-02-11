!pip install scikit-bio #install package for phylogenetic reconstructions

# import packages for phylogenetic inferences
from skbio import DistanceMatrix
from skbio.sequence.distance import hamming
from skbio.tree import nj
import skbio.sequence

import pandas as pd # for data wrestling
import numpy as np # for numeric computation
from google.colab import files # for file upload & download

uploades = files.upload() # upload your distance matrix here

df = pd.read_excel(r"matrix.xlsx") # turn .xlsx file into data frame

Taxa = df.iloc[:, 0] # select taxon names
Characters = df.iloc[:, 1:] # select character vaues

# To create a Sequence object, we need to change the type of the character values recognized by pandas
sequences_str = Characters.values.astype(np.uint8)

# Create a list of objects of the type Sequence (speficif to scikit-bio)
sequences = [skbio.sequence.Sequence(seq) for seq in sequences_str]

# Calculate pairwise distances using Hamming distance
num_sequences = len(sequences)
distances = np.zeros((num_sequences, num_sequences))
for i in range(num_sequences):
    for j in range(num_sequences):
        distance = hamming(sequences[i], sequences[j])
        distances[i, j] = distance
        distances[j, i] = distance

# Convert the pairwise distances into scikit-bio's distance matrix object
distance_matrix = DistanceMatrix(distances, ids=Taxa)

# Create a tree using the neighbor-joining algorithm
tree = nj(distance_matrix)

# Export the tree into the Newick format that can be read by various programs
newick_string = tree.write("tree.newick")

# now you can download the tree file on the left sidebar

"""# New Section"""