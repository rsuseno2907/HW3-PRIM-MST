import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        S = set() # list of visited nodes
        T = [] # the actual tree
        s = 0
        S.add(s)

        # Create a priority queue
        pq = []
        for v, w in enumerate(self.adj_mat[s]):
            if w>0: # skip disconnected vertex
                heapq.heappush(pq, (w, s, v)) # push the weight, the node, and the vertex to pq
        # print(pq)

        while pq:
            # print(pq)
            w, u, v = heapq.heappop(pq) # from the given priority queue, 
                                        # can use heappop to find the one with lowest weight
            if v in S: # skip loop if node is already visited
                # print('meow',pq)
                continue
            
            
            #now actually update the Tree and update S with node that's been visited
            S.add(v)
            T.append((u,v,w))
            # print(T)

            # This step updates the priority queue based on the updated nodes that are in S
            for next_v, next_w in enumerate(self.adj_mat[v]):
                heapq.heappush(pq, (next_w, v, next_v)) 
                # print(next_v,next_w)
            # print(pq)
            # break
        
        # Turn the tree (T) into an adjacency matrix
        # print(self.adj_mat)
        # print(T)
        mst_mat = np.zeros((len(self.adj_mat), len(self.adj_mat)))
        for t in T: 
            # t[0] is node 1, t[1] is node 2, and t[2] is the weight
            mst_mat[t[0],t[1]]=t[2]
            mst_mat[t[1],t[0]]=t[2]
        # print(mst_mat)
        self.mst = mst_mat


# graph_object = Graph('../data/small.csv')
# graph_object.construct_mst()
# # print(graph_object.mst)
# tmp = graph_object.mst
# print(tmp)
# tmp[:] = 1
# print(tmp)
