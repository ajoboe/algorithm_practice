# divide into two halves
# each half is sorted
# merge them back into sorted order
# base case is list of length 1--already sorted
import random

def merge_sort(l):
  merge_sort_helper(l, 0, len(l)-1)

def merge_sort_helper(arr, l, r):
  if r-l > 1:
    m = l + (r-l) // 2
    return merge(merge_sort_helper(arr, l, m), merge_sort_helper(arr, m+1, r))
  else:
    return arr

def merge(left, right):
  arr = []
  while len(left) > 0 and len(right) > 0:
    print("LEFT")
    print(left)
    print("RIGHT")
    print(right)
    print("ARR")
    print(arr)
    if left[0] < right[0]:
      arr.append(left.pop(0))
    else:
      arr.append(right.pop(0))
  arr + left
  arr + right
  return arr

def main():
  l = random.sample(range(100), 20)
  print(l)
  merge_sort(l)
  print(l)

if __name__ == "__main__":
  main()
