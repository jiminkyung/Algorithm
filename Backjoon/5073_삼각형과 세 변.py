"""
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
"""

while True:
    n1, n2, n3 = map(int, input().split())
    
    if n1 == 0:
        break

    n_lst = [n1, n2, n3]
    cnt = len(set(n_lst))

    if sum(n_lst)-max(n_lst) <= max(n_lst):
        print("Invalid")
    else:
        if cnt == 1: print("Equilateral")
        elif cnt == 2: print("Isosceles")
        else: print("Scalene")