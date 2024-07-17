# 누적 합

# 50점
# 메모리: 31120KB / 시간: 116ms
from sys import stdin


input = stdin.readline
S = input()
q = int(input())

def checking(char, l, r):
    cnt = 0

    for i in range(l, r+1):
        if S[i] == char:
            cnt += 1
    
    return cnt

for _ in range(q):
    char, l, r = input().split()
    print(checking(char, int(l), int(r)))


# dp로 풀어보기(with AI teacher) => 50점?
# 메모리: 31120KB / 시간: 52ms
from sys import stdin


input = stdin.readline
S = input().strip()
q = int(input())

dp = [[0] * (len(S) + 1) for _ in range(26)]
a = ord("a")

for i, char in enumerate(S, start=1):
    for j in range(26):
        dp[j][i] = dp[j][i-1]
    dp[ord(char) - a][i] += 1

def checking(char, l, r):
    char_index = ord(char) - a
    return dp[char_index][r + 1] - dp[char_index][l]

for _ in range(q):
    char, l, r = input().split()
    print(checking(char, int(l), int(r)))


# 딕셔너리 dp로 풀어보기 => 50점.
from sys import stdin

input = stdin.readline
S = input().strip()
q = int(input())

dp = {}

for i, char in enumerate(S, start=1):
    if char not in dp:
        dp[char] = [0] * (len(S) + 1)
    
    for c in dp:
        dp[c][i] = dp[c][i-1]
    dp[char][i] += 1

def checking(char, l, r):
    if char not in dp:
        return 0
    return dp[char][r + 1] - dp[char][l]

for _ in range(q):
    char, l, r = input().split()
    print(checking(char, int(l), int(r)))


# 인터넷을 참고한 100점짜리 풀이.
# 메모리: 93316KB / 시간: 744ms
# 고정 크기 사용, 최소한의 연산(하나의 값만 업데이트)가 주 요인인듯.
import sys


input = sys.stdin.readline

S = input().rstrip()
count = [[0] * 26]

q = int(input())

for i, ch in enumerate(S, start=1):
    count.append(count[len(count) - 1][:])
    count[i][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = input().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)