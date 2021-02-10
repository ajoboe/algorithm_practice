# Bubble Sort
# Time complexity: O(n^2) worst case, O(n) best case
# Space complexity: O(1) aux
# Author: Andrew Jacobson

def bubble_sort(x):
  sorted = False
  j = 1
  while not sorted:   
    sorted = True
    for i in range(len(x)-1):
      if x[i] > x[i+1]:
        sorted = False
        x[i], x[i+1] = x[i+1], x[i]
if __name__ == '__main__':
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
  bubble_sort(l)
  print(l)