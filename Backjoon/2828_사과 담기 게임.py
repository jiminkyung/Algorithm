# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2828

# 왼쪽 M 칸을 차지한다는게...
# M이 2이고 내 위치가 2면 [1, 2]를 차지한다는게 아님. [2, 3]을 차지한다는것. 이것때문에 헷갈림 ㅜㅜ
# 관련 글👉 https://www.acmicpc.net/board/view/108419

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    J = int(input())
    # 사과가 떨어지는 위치 (0-based 처리)
    loc = [int(input())-1 for _ in range(J)]

    # 현재 칸을 포함해서 M칸이니까, -1 처리해줌.
    M -= 1
    pos = M  # 바구니의 오른쪽 끝 위치
    cnt = 0

    for l in loc:
        # 사과가 떨어지는 위치가 바구니의 범위 내라면 이동 X
        if pos - M <= l <= pos:
            continue
        # 바구니보다 오른쪽에 위치한다면(바구니의 오른쪽 끝 기준) 차이만큼 이동. 바구니의 오른쪽 끝을 l에 위치시킴.
        if l > pos:
            cnt += (l - pos)
            pos = l
        # 바구니보다 왼쪽에 위치한다면(바구니의 왼쪽 끝 기준) 차이만큼 이동. 바구니의 왼쪽 끝을 l에 위치시킴.
        # pos 기준은 오른쪽 끝이니까 이 경우에는 M만큼 더해줘야함.
        else:
            cnt += (pos - (l + M))
            pos = l + M
        
    
    print(cnt)


main()