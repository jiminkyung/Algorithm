# 문제집 - 0x03강 - 배열


# 문제: https://www.acmicpc.net/problem/1919
# 메모리: 32412KB / 시간: 36ms
s1, s2 = {}, {}
ret = 0

for s in input():
    s1[s] = s1.get(s, 0) + 1

for s in input():
    s2[s] = s2.get(s, 0) + 1

for i in range(97, 123):
    s = chr(i)
    ret += abs(s1.get(s, 0) - s2.get(s, 0))

print(ret)


# 한번만 탐색하면 되는 풀이.
# 출처: https://www.acmicpc.net/source/83327006
import sys
input = lambda : sys.stdin.readline().rstrip()

a = input()
b = input()

res = 0
lst = [0]*26
for c in a :
    lst[ord(c) - 97] += 1
    res += 1

for c in b :
    i = ord(c) - 97
    
    if lst[i] == 0 :
        res += 1
    else :
        lst[i] -= 1
        res -= 1

print(res)