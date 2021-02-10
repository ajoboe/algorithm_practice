'''
This is an implementation of the adjacency-list representation of a graph
where the vertices are numbered from 0 through n-1.

The class has integer variables recording the number n of vertices
and number m of edges.  It has a list ._verts of length n of lists of integers.
The list that appears in position i of this list is the list of neighbors
of vertex i.  For example, if ._verts is [[1,2], [], [0]], then
there are three vertices, since there are three lists in it.  Vertex 0
has neighbors 1 and 2, vertex 1 has no neighbors, and vertex has 0 as
its only neighbor.
'''
class WGraph(object):

  # return number of vertices
  def getn(self):
     return len(self._verts)

  # return number of edges
  def getm(self):
     return self._m

  def neighbors(self, i):
    return self._verts[i]

  # return a list of ordered pairs giving the edges of the graph
  def getEdges(self):
     edgeList = []
     for i in range(self.getn()):
        for j in self.neighbors(i):
           edgeList.append((i,j))
     return edgeList
        
  ''' constructor.  __init__ is a reserved keyword identifying it
      as a constructor.  numVerts tells how many vertices it should have.  
      edgeList is a list of ordered pairs, one for each edge, in any order.
      Example: numVerts = 3 and edgeList = [(0,1), (1,2), (0,2), (2,0)]'''
  def __init__ (self, numVerts, edgeList):
    self._m = len(edgeList)
    self._verts = [[] for i in range(numVerts)]
    for u, v, w in edgeList:
      self.neighbors(u).append((v,w))  # works because neighbors returns a reference
                                       #  to the neighbor list

  # add an edge from tail to head.  No checking for errors, such as multi-edges
  def addEdge(self, tail, head, weight):
    self.neighbors(tail).append((head, weight))
    self._m += 1
  
  ''' String representation of the graph.  If G is an instance of the class,
      this is called with str(G).  It is called implicitly when a string
      is expected, e.g. in a call to print(G) '''
  def __str__(self):
     return 'n = ' + str(self.getn()) + ' m = ' + str(self.getm()) + '\n' + str(self._verts)


  ''' DFS.  colored[j] = True if vertex j is colored, and it's False if j is 
      white.  The parameter i is the vertex number of the vertex to start 
      at, and it must be white '''
  def dfs(self, i, colored):
    colored[i] = True
    for j in self.neighbors(i):
      if not colored[j]:
        self.dfs(j, colored)

'''  Read a graph in from a file.  The format of the file is as follows:
     The first line gives the number of vertices.
     Each subsequent line gives an ordered pair of vertices, separated by
     a comma, indicating a directed edge.

     Example:
     ----
     3
     0,1,4
     1,2,2
     0,2,7
     2,0,1
     ----

     This gives a graph with three vertices and four directed edges,
     (0,1,4), (1,2,2), (0,2,7), (2,0,1)
'''

def readGraph(filename):
  edgeList = []
  fp = open(filename, 'r')
  n = int(fp.readline())
  for line in fp:
     u,v,w  = [int(x) for x in line.split(',')]
     edgeList.append((u,v,w))
  return Graph(n, edgeList)
    

