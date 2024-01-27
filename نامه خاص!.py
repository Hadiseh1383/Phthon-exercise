numbers = input()
sum= int(input())
numlist = numbers.split()
dictionary= dict()
findict = dict()
for index,item in enumerate(numlist):
	dictionary[int(item)]=index
for i in dictionary.keys():
	result= sum - i
	if result in dictionary and result!=i:
		sum1= dictionary[i]+dictionary[result]
		if (result,i) not in findict.keys():
			findict[(i,result)]=sum1
final= sorted(findict.values())
if not findict:
	print("Not Found!")
else:
	for k in final:
		print(k)