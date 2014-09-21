N,sum1,sum2 = 100,0,0
for i in range(1, N + 1):
	sum1 += i
	sum2 += pow(i,2)
print pow(sum1,2) - sum2

