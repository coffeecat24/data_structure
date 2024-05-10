def iFib(n):
	if n<2:
		return 0
	for i in range(2,n+1):
		pp=1
		p=1
		current=pp+p
		pp=p
		p=current
	return current
	
def rFib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return rFib(n-2)+rFib(n-1)
			
print('iFib : %d' %(iFib(3)))
print('rFib : %d' %(rFib(3)))