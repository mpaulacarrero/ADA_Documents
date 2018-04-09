#Estudiante: Maria Paula Carrero Rivas
#UVA Problem: 10245 - The Closest Pair Problem
from sys import stdin
import math
MAX = 10001
EPS,points= 1e-9,None
aux = [ None for i in range(MAX//2) ]

def distance(p1, p2):
  answer =math.hypot(p1[0] - p2[0],p1[1] - p2[1])
  return answer

def solve(low, hi):
  global points, aux
  mid = low + ((hi-low)>>1)
  puntoMid = points[mid]
  sumita= (hi-low)
  ans = float('inf')
  if sumita < 2:
    return float('inf')
  elif sumita == 2:
    ans = distance(points[0], points[1])
  elif sumita==3:
    di1=distance(points[0], points[1])
    di2=distance(points[0], points[1])
    di3=distance(points[0], points[1])
    ans=min(di1,di2,di3)  
  else:
      k = 0
      answer1 = solve(low, mid)
      answer2 = solve(mid, hi)
      ans = min(answer1, answer2)
      for i in range(low,hi):
        if(puntoMid[2] == points[i][2]):
          continue
    #if points[i][0] <= puntomid+ans and points[mid][0] >= puntomid-ans:
        if (abs(puntoMid[0] - points[i][0]) < ans):
          aux[k]=points[i]
          k+=1
      aux[k] = puntoMid
      k+=1
      d = 0
      for i in range(k):
        for j in range(i, k):
          if aux[j][2] == aux [i][2]:
            continue
          d = distance(aux[j],aux[i])
          ans = min (ans, d)
      k == 0 
  return ans

def main():
  global points
  n = int(stdin.readline())
  while n!=0:
    points = list()
    for i in range(n):
      tok = stdin.readline().split()
      points.append((float(tok[0]),float(tok[1]), i))
      #pointsOrd.append(points[-1])
    points.sort(key=lambda x: (x[0], x[1]))
    #for i in range (len(points)): points[i][2]= i 
    #pointsOrd.sort(key=lambda x: x[1])
    ans = solve(0, n)
    if (ans + EPS < 10000):
      print('{:.4f}'.format(ans))
    else:
      print('INFINITY')
    n = int(stdin.readline())

main()
