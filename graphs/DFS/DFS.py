# BFS uses a queue, should DFS use a stack?
from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def DFS(self, start):
    stack = []
    visited = [False] * len(self.graph)

    stack.append(start)
    while stack:
      node = stack.pop(0)
      if not visited[node]:
        visited[node] = True
        print("Visiting " + str(node))
        stack += self.graph[node]


def main():
  g = Graph()
  g.add_edge(0, 1)
  g.add_edge(0, 2)
  g.add_edge(1, 2)
  g.add_edge(2, 0)
  g.add_edge(2, 3)
  g.add_edge(3, 3)
  g.DFS(0)

if __name__ == "__main__":
  main()
