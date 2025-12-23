# 구현
# 문자열
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3048
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N1, N2 = map(int, input().split())

    g1 = input().rstrip()
    g2 = input().rstrip()
    T = int(input())

    # 한 줄로 붙여주기
    line = list(g1[::-1]) + list(g2)
    g1 = set(g1)
    g2 = set(g2)
    time = 0

    # 목적시간에 도달할때까지 개미 이동
    while time < T:
        # line을 그대로 사용할경우, 이미 이동한 개미도 조건에 걸리게 되므로 복제본 생성.
        new_line = line[:]
        for i in range(N1 + N2 - 1):
            # → ← 일때만 바꿔줌
            if line[i] in g1 and line[i+1] in g2:
                new_line[i], new_line[i+1] = new_line[i+1], new_line[i]
        
        line = new_line[:]
        
        time += 1
    
    print(*line, sep="")


main()