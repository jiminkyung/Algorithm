# 구현
# 시뮬레이션
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1817
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 이게 왜 그리디로 분류되는지 잘 모르겠음.
    # 순서대로 박스에 집어넣고, 용량 초과 시 새 박스를 준비하는 방식임.
    N, M = map(int, input().split())
    box = list(map(int, input().split()))

    cnt = curr = 0

    for b in box:
        if curr + b <= M:
            curr += b
        else:
            cnt += 1
            curr = b
    
    cnt += int(curr != 0)  # 다 채워지면 박스를 카운트하는 방식임. 마지막에 카운팅 안 된 박스가 있다면 1, 없다면 0
    print(cnt)


main()