""" UnionFind.py
a union-find data structure by andrew jacobson
"""

class UF:
 # constructor
 def __init__(self, n):
  self.__id = range(0, n)
  self.__l = [[i] for i in range(n)]

 def getn(self):
  return len(self.__l)

 def __str__(self):
  return 'id: ' + str(self.__id) + '\nl' + str(self.__l)

 def find(self, x):
  return self.__id[x]

 def union(self, x, y):
  x_grp = self.find(x)
  y_grp = self.find(y)
  if x_grp == y_grm:
   return False
  else:
   if len(self.__l[x_grp]) < len(self.__l[y_grp]):
    self.__l[y_grp].extend(self.__l[x_grp])
    for i in self.__l[x_grp]:
     self.__id[i] = y_grp
    self.__l[x_grp] = None
   else:  # if y is shorter or they're the same
    self.__l[x_grp].extend(self.__l[y_grp])
    for i in self.__l[y_grp]:
     self.__id[i] = x_grp
    self.__l[y_grp] = None
   return True



if __name__ == '__main__':
 uf = UF(10)
 print 'uf:'
 print(uf)
 print('n = ' + str(uf.getn()))
