def adad_aval(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
a, b = map(int, input().split())
num = 0
for x in range(min(a, b), max(a, b) + 1):
    if adad_aval(x):
        num += 1
if a <= b:
    print(f'main order - amount: {num}')
else:
    print(f'reverse order - amount: {num}')
