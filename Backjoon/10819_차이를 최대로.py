# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/10819

# 처음엔 |A[0] - A[1]| + |A[2] - A[3]| + ... + |A[N-2] - A[N-1]| 인줄알고 오름차순/내림차순대로 번갈아가며 계산을 시도했다.
# => 반만 맞았던 시도였다. 절반까지 번갈아가며 계산하는것은 맞으나,
# => |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|이기 때문에 값을 두배로 계산해야한다.
# => 또한 리스트의 맨 앞,뒤 요소는 한번씩만 계산되므로 더한 값에서 중간값을 한번 빼줘야한다.
# 관련 풀이는 아래에 추가로 기재.

# permutations로 순열을 생성하여 구하는 방법으로 풀이
# 메모리: 31120KB / 시간: 124ms
from sys import stdin
from itertools import permutations


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

ret = 0

for perm in permutations(A):
    tmp = 0
    for i in range(N-1):
        tmp += abs(perm[i] - perm[i+1])
    ret = max(ret, tmp)

print(ret)


# 28ms인 코드를 참고한 풀이.
# 참고: https://www.acmicpc.net/source/82156215
# 발상까지는 맞았는데... 좀 더 길게 생각해볼걸 그랬다...
from sys import stdin


input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()
mid = N // 2

ret = 0
for i in range(mid):
    ret += A[N-i-1] - A[i]

ret *= 2

if N % 2 == 0:
    ret -= A[mid] - A[mid-1]
else:
    ret -= min(A[mid] - A[mid-1], A[mid+1] - A[mid])

print(ret)