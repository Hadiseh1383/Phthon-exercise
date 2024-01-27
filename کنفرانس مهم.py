n = int(input())
domains = set()
for _ in range(n):
	email = input()
	if "@" in email:
		domain = email.split('@')[1]
		domains.add(domain)
result=sorted(domains)
for item in result:
	print(item)