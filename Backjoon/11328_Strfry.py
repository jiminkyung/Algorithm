# 문제집 - 0x03강 - 배열


# 문제: https://www.acmicpc.net/problem/11328
# 메모리: 32412KB / 시간: 116ms
from sys import stdin


input = stdin.readline

def checking():
    arr = [0] * 26
    cnt = 0
    
    s1, s2 = input().rstrip().split()
    
    if len(s1) != len(s2):
        return "Impossible"
    elif s1 == s2:
        return "Possible"
    
    for s in s1:
        s = ord(s) - 97
        arr[s] += 1
        cnt += 1
    
    for s in s2:
        s = ord(s) - 97
        if arr[s] == 0:
            cnt += 1
        else:
            arr[s] -= 1
            cnt -= 1
    
    return "Possible" if cnt == 0 else "Impossible"
    
    
for _ in range(int(input())):
    print(checking())


# all, any 사용
# count가 생각보다 빠르다...?
# 출처: https://www.acmicpc.net/source/83292636
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print('Possible' if all(a.count(i) == b.count(i) for i in set(a)) else 'Impossible')