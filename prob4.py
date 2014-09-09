def check_palin(num):
	s = str(num)
	if s == s[-1]:
		return True
	else:
		return False
lst = []
for i in xrange(100,999):
	for j in xrange(100,999):
		sum=i*j
		if check_palin(sum):
			lst.append(sum)
lst = sorted(lst)
print lst
print lst[0]
print lst[-1]
