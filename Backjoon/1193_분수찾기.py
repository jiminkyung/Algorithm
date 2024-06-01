"""
(홀)1/1
(짝)1/2, 2/1
(홀)3/1, 2/2, 1/3
(짝)1/4, 2/3, 3/2, 4/1
...
"""

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    n1 = X
    n2 = line - X + 1
else:
    n1 = line - X + 1
    n2 = X

print(f"{n1}/{n2}")