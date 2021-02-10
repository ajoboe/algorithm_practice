# Quicksort
import time
def quicksort(x):
  qs_aux(0,len(x),x)
def qs_aux(a,b,x):
  p = a + ((b-a)//2)
  x[p], x[b-1] = x[b-1], x[p]
  lo = 0
  hi = b-2
  while lo < hi:
    print (lo, hi)
    time.sleep(1)
    if x[lo] > x[p]:
      x[lo], x[hi] = x[hi], x[lo]
      hi -= 1
    else:
      lo += 1
  x[p], x[hi] = x[hi], x[p]
  qs_aux(a,p,x)
  qs_aux(p+1,b,x)
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
  quicksort(l)
  print(l)