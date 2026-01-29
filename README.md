[![BuildStatus](https://github.com/rsuseno2907/HW3-PRIM-MST/workflows/HW3-PRIM-MST/badge.svg?event=push)](https://github.com/rsuseno2907/HW3-PRIM-MST/actions)

# Minimum Spanning Tree (Prim's Algorithm)
This repository is written for HW3 of the BMI203 Algorithms class assignment during Winter quarter of 2026.

Prim's algorithm ran on a given graph to find the Minimum Spanning Tree (MST).

## What this project does
- Loads a graph from an adjacency matrix or single-cell data
- Uses Prim's algorithm to find the MST
- Returns the MST as an adjacency matrix (stored in `self.mst`)
- Run GitHub Actions (unit tests) automatically on every push

## Files
- `mst/graph.py`: Graph class and Prim's MST function implementation
- `test/test_mst.py`: Unit tests for MST
- `data/`: Input data, which includes 
	- a small example graph `small.csv`, 
	- single cell data from Slingshot R package `slingshot_example.txt`,
	- two disconnected graphs that are stored within one adjacency matrix `disconnected.csv`

## Packages (Python 3.11)
- pytest
- heapq
- sklearn.metrics
- Union