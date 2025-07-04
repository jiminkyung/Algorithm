# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1639
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    S = list(map(int, input().rstrip()))
    L = len(S)

    # 길이가 1이라면 0 반환
    if L == 1:
        print(0)
        return
    
    max_len = 0

    # i: 검사할 길이 (2N)
    for i in range(2, L+1, 2):
        for j in range(0, L-i+1):
            # 왼쪽 N개, 오른쪽 N개를 체크
            left = S[j:j+i//2]
            right = S[j+i//2:j+i]
            if sum(left) == sum(right):
                max_len = i
                break
    
    print(max_len)


main()