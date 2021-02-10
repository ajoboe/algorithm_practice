# to run type  :! clear; python %
# or           :w !python

def search(l, i):
  return searchHelper(l, i, 0, len(l) - 1)

def searchHelper(l, i, first, last):
  size = last - first + 1
  mid = first + size // 2

  # Base case #1: empty list
  if size == 0:
    return -1

  # Base Case #2: found item
  if l[mid] == i:
    return l[mid]

  # If the item is smaller, go left
  if i < l[mid]:
    return searchHelper(l, i, first, mid - 1)
  # If it's bigger, go right
  else:
    return searchHelper(l, i, mid + 1, last)

def main():
  l = [1, 2, 4, 6, 7, 9, 15, 44, 66, 86, 99, 101, 345, 564, 566, 566, 666, 777, 800, 801, 802, 803, 808, 999]
  needle = 99
  found = search(l, needle)
  print("needle was: " + str(needle))
  print("found:      " + str(found))

  return 0

if __name__ == '__main__':
  main()
