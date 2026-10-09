a = int(input())
b = int(input())
if a == 0:
    if b == 0:
        print("VSN")
    else:
        print("VN")
elif b == 0:
    x = 0
else:
    x = a/b
print(x)
