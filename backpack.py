from sys import stdin
#Estudiante: Maria Paula Carrero Rivas
#Trabajado con Juan Fernando Escobar
#UVA Problem: 907 - Winterim Backpacking Trip
MAX = 610
sites = [ None for i in range(MAX) ]
sums,n,k, maximum = None,None,None,None

def solve():
  global sites,n,k, maximum, sums
  low, hi, mid = 0, sums, 0
  while low+1 != hi :
    mid = low + ((hi-low)>>1)
    newsum, i, noches = 0, 0, 0
    while i < n:
      if (mid < maximum):
        noches = k+1
        i = n
      elif (newsum + sites[i] > mid):
        newsum = sites[i]
        noches += 1
        i +=1
      else:
        newsum += sites[i]
        i +=1
    if (noches <= k):
      hi = mid
    else:
      low = mid
  return hi

def main():
  global sites,n,k, maximum, sums
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    sums, maximum = 0, 0
    for i in range(n):
      sites[i] = int(inp.readline())
      if (sites[i] > maximum) :
        maximum = sites[i]
      sums += sites[i]
    if (sums != 0):
      print(solve())
    else:
      print(0)
    l = stdin.readline().strip()

main()
