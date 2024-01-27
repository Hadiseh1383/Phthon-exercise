def made(n): 
		return "{0:b}".format(int(n)) 
a=input( ) 
b=input( ) 
ba=str(made(a))
bb=str(made(b)) 
ba= (str(10**(100-len(ba)))+ba)
num = 0
bb =(str(10**(100-len(bb)))+bb)
for i in range(101):
	  if ba[-i] != bb[-i]:
	     num +=1
print(num)
