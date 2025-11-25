# 자료 구조
# 스택


# 문제: https://www.acmicpc.net/problem/2841

# 스택 활용 문제
# 메모리: 32412KB / 시간: 420ms
from sys import stdin


input = stdin.readline

def main():
    N, P = map(int, input().split())

    # 각 줄별로 몇번 프랫을 누르고있는지 저장
    stack = [[] for _ in range(7)]
    cnt = 0

    for _ in range(N):
        string, fret = map(int, input().split())

        # 만약 현재 줄에서 누르고 있는 프랫이 있고, 그 프랫이 주어진 프랫보다 높다면 손가락을 떼야 함.
        while stack[string] and stack[string][-1] > fret:
            stack[string].pop()
            cnt += 1
        
        # 이미 누르고 있던 프랫이라면 넘어감.
        if stack[string] and stack[string][-1] == fret:
            continue
        
        # 누르기
        stack[string].append(fret)
        cnt += 1
    
    print(cnt)


main()