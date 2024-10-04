# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/2621
# 메모리: 31120KB / 시간: 32ms
from sys import stdin


input = stdin.readline

colors = []
numbers = []

for _ in range(5):
    color, num = input().rstrip().split()
    colors.append(color)
    numbers.append(int(num))

score = []

max_num = max(numbers)

# 조건 5 (연속적인 숫자일때)
is_True = True
num = sorted(numbers)
prev = num[0]

for n in num[1:]:
    if n == prev + 1:
        prev = n
        continue
    is_True = False
    break

if is_True:
    score.append(max_num + 500)

# 조건 1, 4
if len(set(colors)) == 1:
    # 조건 4 (같은 색상일때)
    score.append(max_num + 600)
    if is_True:  # 조건 1 (같은 색상 + 연속적인 숫자일때)
        score.append(max_num + 900)

cnt_num = {numbers.count(i): i for i in set(numbers)}  # 갯수가 같으면 겹침
num_cnt = {i: numbers.count(i) for i in set(numbers)}  # 숫자가 같으면 겹침

# 조건 2 (4장의 숫자가 같을때)
if 4 in cnt_num:
    score.append(cnt_num[4] + 800)
    # 조건 7 (2장/2장 같을때), 조건6,8은 조건2값이 무조건 크므로 pass
    score.append(cnt_num[4] * 11 + 300)

# 조건 3, 6
elif 3 in cnt_num:
    score.append(cnt_num[3] + 400)  # 조건 6 (3장의 숫자가 같을때)
    if 2 in cnt_num:  # 조건 3 (3장/2장 같을때)
        score.append(cnt_num[3] * 10 + cnt_num[2] + 700)
        # 조건 7
        num1 = cnt_num[3]
        num2 = cnt_num[2]
        if cnt_num[3] < cnt_num[2]:
            num1, num2 = num2, num1
        score.append(num1 * 10 + num2 + 300)

# 조건 7, 8
elif 2 in cnt_num:
    num1 = num2 = cnt_num[2]

    for k in num_cnt:
        if num_cnt[k] == 2 and k != num1:
            num2 = k
            break
    if num1 == num2:  # 조건 8 (2장의 카드가 같을때)
        score.append(num1 + 200)
    else:  # 조건 7 (2장/2장 같을때) - 키값 중복으로 하나의 2만 들어간 상태
        if num1 < num2:
            num1, num2 = num2, num1
        score.append(num1 * 10 + num2 + 300)

# 조건 9 (아무것도 해당되지 않을때)
else:
    score.append(max_num + 100)

print(max(score))


# 메모리/실행시간은 다들 비슷하나, 코드길이가 확연히 짧은 풀이가 있었다.
# 유니온 파인드를 그렇게 풀어놓고 왜 생각을 못했는지...
import sys
input = sys.stdin.readline

A = []
N = []
C = [0 for i in range(10)]

for i in range(5):
    x = list(map(str, input().split()))
    A.append(x[0])
    N.append(int(x[1]))
    C[N[i]] += 1

N.sort()

if A[0] == A[1] == A[2] == A[3] == A[4] and N[0]+4 == N[1]+3 == N[2]+2 == N[3]+1 == N[4]:
    print(900+N[-1])
elif max(C) == 4:
    print(800 + C.index(4))
elif 3 in C and 2 in C:
    print(C.index(3)*10 + C.index(2) + 700)
elif A[0] == A[1] == A[2] == A[3] == A[4]:
    print(600 + N[-1])
elif N[0]+4 == N[1]+3 == N[2]+2 == N[3]+1 == N[4]:
    print(500 + N[-1])
elif 3 in C:
    print(400 + C.index(3))
elif C.count(2) == 2:
    x = [0, 0]
    y = 0

    for i in range(len(C)):
        if C[i] == 2:
            x[y] = i
            y += 1
    print(x[1]*10 + x[0] + 300)
elif C.count(2) == 1:
    print(200 + C.index(2))
else:
    print(100 + N[-1])