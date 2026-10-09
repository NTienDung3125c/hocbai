a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == d and b == c) or (a == c and b == d) or (a == b and d == c):
    print("YES")
else:
    print("NO")
