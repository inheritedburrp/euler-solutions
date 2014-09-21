sum = 2

def fibonacci(n):
	global sum
	lst = [1,2]
	for i in xrange(0,n-2):
		lst.append(int(lst[-1])+int(lst[-2]))
		
		if lst[-1] % 2 == 0:
			sum += lst[-1]
		elif lst[-1] > 4000000:
			return
		

fibonacci(32)
print sum
