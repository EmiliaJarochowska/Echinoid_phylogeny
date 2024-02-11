from Bio.Phylo.TreeConstruction import DistanceMatrix
from scipy.spatial.distance import pdist


import pandas as pd # for data wrestling
import numpy as np # for numeric computation

df0 = pd.read_excel(r"Python/Lecture_example.xlsx") # turn .xlsx file into data frame
df = df0.T

Taxa = df.index.tolist()[1:] # select taxon names
Characters = df.iloc[1:, :] # select character vaues

# We need to change the type of the character values recognized by pandas
sequences_str = Characters.values.astype(np.uint8)

# Compute pairwise Euclidean distances
distances = pdist(sequences_str, metric='euclidean')

# Print the distance matrix
print(distances)

n = len(sequences_str)

# pdist returns a condensed distance matrix, but we need a lower triangular list of lists
matrix_data = [[] for _ in range(n-1)]

index = 0
for i in range(1, n):
    for j in range(i):
        matrix_data[i-1].append(distances[index])
        index += 1

# Convert the matrix_data to a list of numerical lists
matrix_data = [list(row) for row in matrix_data]

# Create a BioPython DistanceMatrix object
matrix = DistanceMatrix(Taxa, matrix_data)
# Doesn't work: Taxa has length 5, sequences_str has length 5, distances has 10, matrix_data has 4 - does not match