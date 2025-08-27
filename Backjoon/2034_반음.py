# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2034
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 도 ~ 시까지 반음을 포함한 음계
    scale = ["C", 0, "D", 0, "E", "F", 0, "G", 0, "A", 0, "B"]

    n = int(input())
    sheet = [int(input()) for _ in range(n)]
    ret = []

    # 여러 경우가 가능할 경우, 알파벳이 작은 순서부터 출력해야 함.
    # A, B, C (라, 시, 도...) 순서로 시작 음 체크
    for start in (9, 11, 0, 2, 4, 5, 7):
        end = start
        for nxt in sheet:
            end = (end + nxt) % 12
            if scale[end] == 0:  # 반음에 해당되면 break
                break
        else:
            ret.append((scale[start], scale[end]))
    
    for line in ret:
        print(*line)


main()