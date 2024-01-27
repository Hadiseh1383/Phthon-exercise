n = int(input())
row =[1]
for i in range(n):
	if i>=1:
		row =[1]+ [row[j] + row[j+1] for j in range(len(row)-1)]+ [1]
		print(' '.join(map(str, row)))
	else:
		print(' '.join(map(str,row)))
