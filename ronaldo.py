n , m = map(int, input().split())
if n > m :
    cc = m
    cm = (n - m)//2
else:
    cc = n
    cm = (m - n)//2
print(cc,cm)
