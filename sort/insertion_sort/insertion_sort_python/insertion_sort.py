import random

def insertion_sort(l):
  for i in range(1, len(l)):
    tmp = l[i]
    j = i-1
    while tmp < l[j] and j >= 0:
      l[j+1] = l[j]
      j -= 1
    l[j+1] = tmp

def main():
  l = random.sample(range(100), 20)
  print(l)
  insertion_sort(l)
  print(l)

if __name__ == "__main__":
  main()
