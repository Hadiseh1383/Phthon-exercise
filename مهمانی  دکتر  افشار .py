a=int(input())
b=int(input())
k=int(input())
while k :
	i=int(input())
	if i<32 :
		if a & (1 << i):
			print("yes")
		else:
			print("no")
	else :
		if b & (1 << (i-32)) :
			print("yes")
		else:
			print("no")
	k -= 1	
	if k==0:
		break
