a, b = map(int, input().strip().split())
for i in range(b):
    s = ""
    for k in range(a):
        s += "*"
    print(s)