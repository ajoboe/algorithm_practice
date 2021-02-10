'''
def insertion_sort(x):
  for i in range(len(x)):
    for j in range(i+1):
      if x[-1] < x[j] or j == i:
        x.insert(j, x.pop())
'''
def insertion_sort(x):
  for i in range(len(x)):
    for j in range(i+1):
      if x[-1] < x[j] or i == j:
        x.insert(j, x.pop())
if __name__ == "__main__":
  l = list()
  l.append(3)
  l.append(7)
  l.append(6)
  l.append(0)
  l.append(2)
  l.append(5)
  l.append(4)
  l.append(9)
  l.append(8)
  l.append(1)
  print(l)
  insertion_sort(l)
  print(l)