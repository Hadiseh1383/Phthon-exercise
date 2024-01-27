def dokme(a,b):
    while b != 0:
        x = a & b
        a = a ^ b
        b = x << 1
    return a
m = int(input())
n = int(input())
k = int(input())
dokme_kharab = dokme(m,n)

if dokme_kharab == k :
    print(dokme_kharab)
    print('YES')
else :
    print(dokme_kharab)
    print('NO')