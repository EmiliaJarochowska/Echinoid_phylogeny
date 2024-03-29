!pip install scikit-bio #install package for phylogenetic reconstructions

# import packages for phylogenetic inferences
from skbio import DistanceMatrix
from skbio.tree import nj

import pandas as pd # for data wrestling
import numpy as np # for numeric computation
from google.colab import files # for file upload & download

uploads = files.upload() # upload your distance matrix here

df = pd.read_excel("matrix.xlsx") # turn .xlsx file into data frame

Taxa = df.iloc[:, 0] # select taxon names
Characters = df.iloc[:, 1:] # select character vaues

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

# Create a tree using the neighbor-joining algorithm
tree = nj(distance_matrix)

# Export the tree into the Newick format that can be read by various programs
newick_string = tree.write("tree.newick")

# now you can download the tree file on the left sidebar

"""# New Section"""