from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
    print('init')

  def add_edge(self, u, v):
    self.graph[u].append(v)
    print("added edge (" + str(u) + ", " + str(v) + ')')

  def BFS(self, start):
    print("Starting at node " + str(start))
    queue = []
    visited = [False] * len(self.graph)

    queue.append(start)
    while queue:
      node = queue.pop(0)
      if(not visited[node]):
        visited[node] = True
        print("visiting node " + str(node))
        queue.extend(self.graph[node])


def main():
  g = Graph()
  g.add_edge(0, 1)
  g.add_edge(0, 2)
  g.add_edge(1, 2)
  g.add_edge(2, 0)
  g.add_edge(2, 3)
  g.add_edge(3, 3)

  g.BFS(2)

if __name__ == "__main__":
  main()
