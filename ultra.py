from sys import stdin
# Estudiante: Maria Paula Carrero Rivas
# Trabajado con Juan Fernando Escobar
#UVA Problem: 10810 - Ultra-QuickSort
MAX   = 50010
num   = [ None for i in range(MAX) ]
aux   = [ None for i in range(MAX) ]
respuesta = 0

def solve(num,low, hi):
	if low+1 < hi:
		mid = low + ((hi-low)>>1)
		solve(num,low, mid)
		solve(num,mid, hi)
		ultrapro(low, mid, hi)

def ultrapro(low,mid, hi):
	global aux, num, respuesta
	for i in range (low, hi): 
		aux[i] = num[i] 
	l,r,i = low, mid, low
	while i != hi:
  		if l!= mid and r!= hi:
  			if aux[l] <= aux[r]:
  				num[i] = aux[l]
  				l+=1
  			else:
  				num[i] = aux[r]
  				r+=1
  				respuesta+= mid-l
  		elif r == hi:
  			num[i] = aux[l]
  			l+=1
  		elif l == mid:
  			num[i]= aux[r]
  			r+=1
  		i+=1

def main():
	global num, respuesta
	inp = stdin
	n = int(stdin.readline().strip())
	while n>0:
		for i in range(n):
			num[i] = int(stdin.readline())
		solve(num,0, n)
		print(respuesta)
		respuesta = 0
		n = int(stdin.readline().strip())	

main()
