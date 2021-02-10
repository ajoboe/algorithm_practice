import random
# O(n^2)
# O(n) if it is already sorted

def bubble_sort(l):
  # make n passes
  for i in range(len(l)):
    sorted = True
    for j in range(1, len(l)):
      if l[j-1] > l[j]:
        temp = l[j-1]
        l[j-1] = l[j]
        l[j] = temp
        sorted = False
    if sorted:
      print("finished early after " + str(i) + " of " + str(len(l)) + " iterations")
      return l
  return l

def main():
  l = random.sample(range(100), 20)
  print(l)
  l = bubble_sort(l)
  print(l)

if __name__ == "__main__":
  main()
