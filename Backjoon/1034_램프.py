# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1034
# 단순히 모든 경우를 계산하면 시간초과다!

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    lamps = [input().rstrip() for _ in range(N)]
    K = int(input())

    # 1. 같은 패턴을 가진 행끼리 묶어주기
    patterns = {}  # patterns[행 패턴] = '행 패턴'과 동일한 행의 갯수
    for row in lamps:
        patterns[row] = patterns.get(row, 0) + 1
    max_lit = 0
    
    # 2. 패턴별로 0의 갯수를 계산하고 K와 비교연산
    for pattern, cnt in patterns.items():
        zeros = pattern.count("0")

        # 만약 0의 갯수가 K보다 크다면 가망없으므로 넘어감
        if zeros > K:
            continue

        # 패턴과 K의 홀짝성이 동일하다면, 스위치를 K번 내로 조작하여 행을 밝힐 수 있다는 뜻
        if zeros % 2 == K % 2:
            max_lit = max(max_lit, cnt)
            if max_lit == N:  # 최댓값이 전체 행의 수와 동일하다면 break
                break
    
    print(max_lit)


main()