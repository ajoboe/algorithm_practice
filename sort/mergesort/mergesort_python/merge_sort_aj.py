def ms(x):
  if(len(x) <= 3):
    x.sort()
    return x
  else:
    mid = len(x) // 2
    return merge(ms(x[:mid]), ms(x[mid:]))
def merge(x, y):
  z = list()
  while (len(x) > 0) or (len(y) > 0):
    if(len(y) == 0):
      z.append(x.pop(0))
    elif(len(x) == 0):
      z.append(y.pop(0))
    elif(x[0] < y[0]):
      z.append(x.pop(0))
    else:
      z.append(y.pop(0))
  return z
if __name__ == "__main__":
  l = list()
  l.append(3)
  l.append(5)
  l.append(2)
  l.append(9)
  l.append(8)
  l.append(1)
  l.append(4)
  l.append(7)
  l.append(6)
  print(l)
  l = ms(l)
  print(l)