# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1713

# 도움이 됐던 반례👉 https://www.acmicpc.net/board/view/122289 (시간 업데이트 지점)
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    T = int(input())
    curr = []
    thumbs = [0] * 101
    times = [0] * 101

    for t, num in enumerate(map(int, input().split())):
        # 1. 해당 학생의 추천수 +1
        thumbs[num] += 1
        
        # 2. 이미 걸려있는 학생이라면 넘어감 (추천수만 증가시키고 걸린 시간은 유지해야함)
        if num in curr:
            continue

        times[num] = t
        # 3-1. 걸려있지 않고, 남아있는 틀이 있다면 걸음
        if len(curr) < N:
            curr.append(num)
        # 3-2. 걸려있지 않고, 남아있는 틀도 없다면
        else:
            # 이미 걸려있는 학생들 중 추천수가 가장 적은, 여러명이라면 오래된 순으로 정렬
            order = sorted(curr, key=lambda x: (thumbs[x], times[x]))
            thumbs[order[0]] = 0  # 해당 학생의 추천수, 걸린 시간을 0으로 변경
            times[order[0]] = 0
            curr_idx = curr.index(order[0])  # 해당 학생의 기존 순서
            curr[curr_idx] = num

    print(*sorted(curr))


main()