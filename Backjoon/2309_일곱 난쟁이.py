# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2309

# 조합 모듈을 사용해도 시간상 큰 차이는 없다.
# 메모리: 31120KB / 시간: 32ms
from sys import stdin
from itertools import combinations


input = stdin.readline

dwarf = sorted(int(input()) for _ in range(9))

for comb in combinations(dwarf, 7):
    if sum(comb) == 100:
        print(*comb, sep="\n")
        break


# 조합을 사용하지 않은 방법들.
# 1: https://www.acmicpc.net/source/83673085
data = []

for _ in range(9):
    height = int(input())
    data.append(height)

x = sum(data) - 100  # x = 아홉난쟁이들의 키 합 - 100

for num in data:
    tmp_a = x - num
    if (tmp_a in data) & (tmp_a != num):  # 어떤 수1 + 어떤 수2 = x 일때
        data.remove(num)
        data.remove(tmp_a)
        break

data = sorted(data)

for i in data:
    print(i)

# 2: https://www.acmicpc.net/source/84050842
L = []
for _ in range(9):
    L.append(int(input()))

one = 0
two = 0
sum_L = sum(L)
for i in range(9):  # 조합과 비슷한 방식으로 순회
    for j in range(i+1, 9):
        if sum_L - L[i] - L[j]== 100:  # 아홉난쟁이들의 키 합 - L[i] - L[j]가 100일때
            one = L[i]
            two = L[j]
L.remove(one)
L.remove(two)
L.sort()
#print(*L)
for i in L:
    print(i)