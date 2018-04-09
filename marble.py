from sys import stdin
#Estudiante: Maria Paula Carrero Rivas
#UVA Problem: 0474 - Where is the Marble?
marble,lenm = None,None

def solve(x):
  # Pre: marble[0..N) is an array of numbers in ascending order and x is a
  # number
  # Pos: Is x in marble[0..N)? If so, in what position?
  global marble,lenm
  ans = False
  if lenm!= 0:
    low, hi = -1, lenm-1
    # P0: (E i | -1 < i < N-1 : A[i]=x) == (E i | low < i <= hi : A[i]=x)
    # P1: -1 <= low < hi <= N-1
    if (lenm == 1): ans = (marble[0] == x)
    while low+1 != hi :
      mid = low + ((hi-low)>>1)
      if marble[mid] >= x:
        hi = mid
      else:
        low = mid
      ans = (marble[hi] == x)
  return ans, hi+1

def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      x = int(inp.readline())
      ans, place = solve(x)
      if ans== False:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,place))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()
