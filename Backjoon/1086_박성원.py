# 동적 계획법 3


# 문제: https://www.acmicpc.net/problem/1086

# 비트마스킹 DP 문제임을 까먹고 푼 코드... 당연히 메모리 초과.
from sys import stdin
from itertools import permutations


input = stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
nums = [input().rstrip() for _ in range(N)]
K = int(input())

perms = list(permutations(nums))
correct = 0

for perm in perms:
    n = int("".join(perm))
    if n % K == 0:
        correct += 1

m = gcd(len(perms), correct)

print(f"{correct // m}/{len(perms) // m}")


# 비트마스킹이 아직 생소해서 어려웠던 문제...
# 참고👉 https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-1086%EB%B2%88-%EB%B0%95%EC%84%B1%EC%9B%90-Java-Python
# 부분마다 뜯어보고 (GPT+스스로)로 질답한뒤에야 이해할 수 있었다.

# 메모리: 110196KB / 시간: 5908ms
from sys import stdin
import math


input = stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
K = int(input())

# remain[i][j] = 현재 나머지가 j일때 i번째 숫자를 추가한 후의 나머지.
# 추가하려는 숫자의 인덱스(i), 이전까지의 나머지(j)
remain = [[(j * 10 ** len(str(S[i])) + S[i]) % K for j in range(K)] for i in range(N)]

# dp[i][j] = 선택한 숫자들(i), 현재까지의 나머지(j)
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for mask in range(1 << N):  # mask: 현재까지 선택한 숫자들(비트마스크)
    for i in range(N):  # i: 현재 고려중인 숫자의 인덱스
        if mask & (1 << i):  # 🚨 if not으로 체크할때보다 더 빠름.
            continue
        for j in range(K):  # j: 현재까지의 나머지
            # remain[i][j] 자체가 "현재 나머지가 j인경우"를 기반으로 i를 추가했을때의 나머지값을 나타낸다.
            # 따라서 이에 따른 경우의 수인 dp[mask][j]를 새로운 dp에 더해줘야 한다.
            dp[mask | (1 << i)][remain[i][j]] += dp[mask][j]

correct = dp[(1 << N) - 1][0]
total = sum(dp[(1 << N) - 1])
m = math.gcd(correct, total)
print(f"{correct // m}/{total // m}")