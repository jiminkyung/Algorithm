# 수학
# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3060
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        print(solve())


def solve() -> int:
    N = int(input())
    lst = list(map(int, input().split()))

    # 첫 날부터 사료량이 부족할경우
    if sum(lst) > N:
        return 1
    
    day = 2
    is_poss = True  # 가능여부
    total = N

    while is_poss:
        total = N  # 오늘치 사료
        new_lst = lst[:]

        for i in range(6):
            # (본돈 + 양 옆 + 맞은편)이 어제 먹은 양
            new_val = lst[(i-1) % 6] + lst[(i+1) % 6] + lst[(i+3) % 6] + lst[i]

            # 현재 남은 사료량으로는 불가능하다면 오늘 배급은 실패.
            if new_val > total:
                is_poss = False
                break

            # 가능하다면 사료량에서 현재 계산한 양을 빼주고, 새 리스트에 저장.
            total -= new_val
            new_lst[i] = new_val 
        else:
            # 문제 없이 배급했다면 날짜 +1
            day += 1

        lst = new_lst[:]
    return day


main()