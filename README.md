## Project structure: 
The project is divided into several files:
- **`dijkstra.py`** - contains implementations of the algorithm and its auxiliary functions
- **`main.py file`** - the main file processing the graph from the file
- **`test_dijkstra.py`** - file with tests for the algorithm and its auxiliary functions
# Installation and startup procedure
1. Clone the repository:
```bash
git clone https://github.com/kpta119/DijkstraAlgorithm.git
```
2. Run the program:
```bash
python3 main.py [filepath]
```
# [filepath] - optional argument - name of the graph file to processing
The running program writes to the console the information found in the graph using the Dijkstra algorithm,
optimal path between zeros. When we do not provide a calling argument
By default, the file opened by the program is graph.txt.
