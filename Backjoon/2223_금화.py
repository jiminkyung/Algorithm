# 수학
# 구현
# 시뮬레이션
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2223

# 거속시 활용까지는 했는데... 계산 과정에서 딴 길로 샜다. 결국 아래 글을 참고함...
# 참고👉 https://www.acmicpc.net/board/view/108975
# 다시 풀어봐야하는 문제.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # t: 시간, x: 시간당 획득량
    t, x, m = map(int, input().split())
    min_time = int(1e9)
    
    # (d, s): (거리, 속력)
    for _ in range(m):
        d, s = map(int, input().split())
        # d가 s로 딱 나누어 떨어지는 순간 == 지민이가 몬스터에게 잡힘.
        # min_time = 최대 연속으로 "안전하게" 금화를 주울 수 있는 한계 시간
        # 따라서 (d-1) // s가 해당 몬스터에게서 안전하게 금화를 주울 수 있는 시간이 된다.
        # -> 한계시간이 가장 짧은 몬스터를 타겟으로 삼고, 이 몬스터를 기준으로 행동한다.
        min_time = min(min_time, (d-1) // s)
    
    if min_time == 0:
        print(0)
    elif min_time >= t:
        print(t * x)
    else:
        # 남은 시간동안은 기다렸다/주웠다를 반복해야함.
        # 두 동작을 한 셋트로 취급. 기다리는게 먼저이므로 남은 시간을 // 2 한 값이 주울 수 있는 시간.
        rest_time = (t - min_time) // 2
        print((min_time + rest_time) * x)


main()