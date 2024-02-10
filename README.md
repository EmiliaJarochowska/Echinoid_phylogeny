## Open Educational Resource (OER)
# Construct a phylogenetic tree from morphological character data

Target audience: University students (BSc) inn Earth Sciences or Biology

Discipline: Earth sciences, geoscience, Evolutionary biology

### Usage

The exercise assumes that you have a character matrix in `.xlsx` format. The first column are names of taxa.
You can run the script in `Python/Phylogenetic_tree.py` to import this matrix into Python, use [`scikit-bio`](https://scikit.bio/) to create a tree using the neighbor-joining method and save the tree in the [Newick format](https://en.wikipedia.org/wiki/Newick_format). 

The script assumes that there is a `matrix.xlsx` file in the same folder as the script, so in `Python`. You can copy your matrix into that folder and make sure it's called `matrix.xlsx` or change the path in the script.

The script saves a tree file called `tree.newick` in the same folder. You can view this filed using many software packages for phylogenetic analyses, as well as online using ETE's [TreeViewer](http://etetoolkit.org/treeview/).

### Running instructions

#### Option 1: Running in a virtual environment using poetry

Activate the virtual environment by typing the following in your terminal:
```
poetry install
```
after that you can type:
```
poetry run python Python/Phylogenetic_tree.py
```

*** TBC: add options for users not familiar with venvs ***

### How to contribute 
If you would like to contribute to this OER, please see [CONTRIBUTING.md](CONTRIBUTING.md).

### License
Please see [LICENSE.md](LICENSE.md)

### Author
__Emilia Jarochowska__  
Utrecht University  
email: e.b.jarochowska [at] uu.nl  
Web page: [www.uu.nl/staff/EBJarochowska](https://www.uu.nl/staff/EBJarochowska)  
ORCID: [0000-0001-8937-9405](https://orcid.org/0000-0001-8937-9405)

__Niklas Hohmann__  
Utrecht University  
email: n.h.hohmann [at] uu.nl  
Web page: [www.uu.nl/staff/NHohmann](https://www.uu.nl/staff/NHHohmann)  
ORCID: [0000-0003-1559-1838](https://orcid.org/0000-0003-1559-1838)

### Copyright
Copyright 2024 Utrecht University
