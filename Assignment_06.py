# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
# This class represents a directed graph using
# adjacency list representation

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # A function used by DFS

    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
        # Recur for all the vertices
        # adjacent to this vertex

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
                # The function to do DFS traversal. It uses
                # recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
        # Driver code
        # Create a graph given
        # in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
# g.addEdge('A','B')
# g.addEdge('A','C')
# g.addEdge('B','C')
# g.addEdge('B','D')
# g.addEdge('D','E')
# g.addEdge('E','B')
# g.addEdge('E','F')
# g.addEdge('F','A')
print("Following is DFS from (starting from vertex A)")
g.DFS(0)



# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.


# from collections import defaultdict
# # This class represents a directed graph
# # using adjacency list representation

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        # function to add an edge to graph

    def addEdge(self,u,v):
        self.graph[u].append(v)
        # Function to print a BFS of graph

    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [0] * (max(self.graph) + 1)
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = 1
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

            for i in self.graph[s]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
                # Driver code
                # Create a graph given in
                # the above diagram

g = Graph()
# g.addEdge('A','B')
# g.addEdge('A','C')
# g.addEdge('B','C')
# g.addEdge('B','D')
# g.addEdge('D','E')
# g.addEdge('E','B')
# g.addEdge('E','F')
# g.addEdge('F','A')
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Breadth First Traversal" " (starting from vertex 2)")
g.BFS('A')

