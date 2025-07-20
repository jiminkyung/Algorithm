# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1758
# 메모리: 36264KB / 시간: 64ms
from sys import stdin


input = stdin.readline

def main():
    # (원래 주려던 팁 - 순서 < 0) 이라면 팁에 변화 없음.
    # 🗝️따라서 팁이 많은 사람부터 내림차순으로 정렬 후 계산해야함. 확실한 이득부터 get~
    # -> 만약 음수값도 전체 팁에 반영한다면, 정렬 할 필요 X.
    N = int(input())
    tips = [int(input()) for _ in range(N)]
    tips.sort(reverse=True)

    ret = 0

    for i, tip in enumerate(tips):
        curr_tip = tip - i

        if curr_tip < 0:
            continue
        ret += curr_tip
    
    print(ret)


main()