def convert(num, base):
	result = " "
	while num> 0:
		digit= num % base
		result = str(digit) + result
		num //= base
	return result
list = [ ]
sum_of_converted_numbers = 0
while True:
	dig=0
	num, base= map(int, input().split())
	if int(num)+int(base)==-2:
	   if sum_of_converted_numbers >0:
	           print('invalid base!')
	           exit()
	   elif sum_of_converted_numbers ==0:
	   	break
	if base <2 or base>=10:
	   sum_of_converted_numbers+=1 
	for i in range(1,num+1):
		if num%i==0:
			dig+=(num//i)
	list.append(convert(dig, base))
sum = 0
for i in range(len(list)):
	sum+= int(list[i])
print(sum)
