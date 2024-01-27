import re
text = input()
text = re.sub(r' +',' ',text.strip())
text = re.sub(r"\\n","\n",text)
result=''
text=list(text)
matn=[ ]
sum = 0
for i in text:
	if i=='@':
		matn.append('@')
		sum+=1
	elif i =='#' and sum>0:
		sum-=1
	else:
		matn.append(i)
for item in matn:
	result+=item
print('Formatted Text: '+result)