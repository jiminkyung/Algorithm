"""
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
"""

angles = []

for _ in range(3):
    p = int(input())
    angles.append(p)

if sum(angles) == 180:
    cnt = len(set(angles))
    if cnt == 1: print("Equilateral")
    elif cnt == 2: print("Isosceles")
    else: print("Scalene")
else:
    print("Error")