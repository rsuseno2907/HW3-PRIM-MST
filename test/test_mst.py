import pytest
import numpy as np
from mst.graph import Graph
from sklearn.metrics import pairwise_distances


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'

    # More assertions
    # MST should always have |V|-1 edges
    edge_count = 0
    mst[mst != 0] = 1 #turn all non-zero values to 1 to get a count of edges
    for i in range(mst.shape[0]):
        for j in range(i+1):
            edge_count += mst[i,j]
    assert edge_count == mst.shape[0]-1

def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """
    On an edge case where there are two disconnected graphs, it should return the 'first' MST
    So we can assert whether the number of nodes of the input graph is greater than the MST
    """
    file_path = './data/disconnected.csv'
    g = Graph(file_path)
    g.construct_mst()
    nodecount_adj = np.sum(np.any(g.adj_mat > 0, axis=1)) # total of 8 nodes
    nodecount_mst = np.sum(np.any(g.mst > 0, axis=1)) # total of 5 nodes
    assert nodecount_adj > nodecount_mst # number of node in the original matrix should be greater than its mst
