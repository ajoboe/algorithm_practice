import random

def mergesort(l):
  # base case: a list of zero or one items is considered sorted
  if len(l) <= 1:
    return l
  # recursive case
  mid = len(l)//2
  left = mergesort(l[:mid])
  right = mergesort(l[mid:])
  return merge(left, right)

def merge(left, right):
  ret = []
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      ret.append(left.pop(0))  # removing from head of list not effecient, use queue
    else:
      ret.append(right.pop(0))
  return ret + left + right

def main():
  l = random.sample(range(100), 20)
  print(l)
  l = mergesort(l)
  print(l)

if __name__ == '__main__':
  main()
