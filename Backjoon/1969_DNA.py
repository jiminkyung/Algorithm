# 구현
# 그리디 알고리즘
# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1969
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    dnas = [input().rstrip() for _ in range(N)]
    # 65 ~ 90: 대문자 A ~ Z의 아스키코드값
    cnt = [[0] * 26 for _ in range(M)]

    # 1. 각 위치에 등장하는 문자 체크
    # cnt[i][j]: i번째 위치의 문자 = chr(j+65) -> A ~ Z
    for dna in dnas:
        for i, alp in enumerate(dna):
            cnt[i][ord(alp)-65] += 1
    
    ret = ""

    # 2. 각 위치에서 가장 많이 등장하는 문자를 ret에 저장
    for i in range(M):
        max_idx = 0
        alp = None
        for j in range(1, 26):
            if cnt[i][j] > cnt[i][max_idx]:
                max_idx = j
        
        ret += chr(max_idx + 65)
    
    # 3. 해밍 거리 계산
    hamming = 0

    for dna in dnas:
        for idx in range(M):
            if ret[idx] != dna[idx]:
                hamming += 1

    print(ret, hamming, sep="\n")


main()