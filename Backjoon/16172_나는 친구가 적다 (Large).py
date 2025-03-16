# 문제집 - 0x1E강 - KMP


# 문제: https://www.acmicpc.net/problem/16172

# 원본 문자열 S는 숫자가 섞여있는 상태. ex) "q123he3knkd"
# 숫자 제거 후 KMP 알고리즘을 실행해야 함.
# re 모듈을 사용하는것보다 제너레이터를 사용하는게 메모리, 시간 모두 효율적임.

# 메모리: 37364KB / 시간: 104ms
from sys import stdin


input = stdin.readline

S = input().rstrip()
K = input().rstrip()

# 원본 문자열 S에서 숫자만 제거
alpha = "".join(a for a in S if a.isalpha())

def make_lps(K: str) -> list:
    n = len(K)
    lps = [0] * n
    length, i = 0, 1

    while i < n:
        if K[length] == K[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                i += 1
    return lps


def kmp(alpha: str, K: str) -> int:
    if not alpha:
        return 0
    
    n, m = len(alpha), len(K)

    if n < m:
        return 0
    
    lps = make_lps(K)

    i = j = 0  # i: alpha 인덱스, j: K 인덱스

    while i < n:
        if alpha[i] == K[j]:
            i += 1
            j += 1
        
        if j == m:
            return 1
        
        if i < n and alpha[i] != K[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return 0


print(kmp(alpha, K))