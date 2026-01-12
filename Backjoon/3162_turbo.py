# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3162

# 조건을 제대로 이해해야 되는 문제...
# 구현 연습용으로 나중에 다시 풀어볼 만함.

# 메모리: 32412KB / 시간: 104ms
from sys import stdin


input = stdin.readline

def main():
    # 1. 채널은 터보 모드를 거칠때마다 리셋되는게 아님. 누적되는 형태.
    # 2. 터보로 표시된 채널도 히스토리에 누적.
    # 3. 사이클의 범위는 터보 진입 직전 채널번호 X의 이전 등장 이후부터 현재 X까지를 중복 없이.
    # ex) [1, 2, 3, 2, 1, 2] -> 2의 직전 등장은 인덱스 3. 사이클은 4~5(중복없이)가 됨.
    N = int(input())

    data = [int(input().replace("T", "0")) for _ in range(N)]
    channel = []
    ret = []

    idx = 0

    while idx < N:
        # 채널 저장
        if data[idx] > 0:
            while idx < N and data[idx] > 0:
                channel.append(data[idx])
                idx += 1
        # 터보 모드 전환
        else:
            last = len(channel) - 1
            prev = -1
            for i in range(last):
                if channel[i] == channel[last]:
                    prev = i
            used = set()

            # last 채널의 직전 등장 이후부터 체크.
            # 만약 last 채널이 이전에 등장 한 적 없다면, -1 + 1 = 0, 처음부터 체크되는거임.
            start = prev + 1
            cycle = []

            # 중복 제거
            for i in range(start, last+1):
                if channel[i] not in used:
                    cycle.append(channel[i])
                    used.add(channel[i])
            
            cycle_idx = 0

            while idx < N and data[idx] == 0:
                ret.append(cycle[cycle_idx])
                channel.append(cycle[cycle_idx])
                cycle_idx = (cycle_idx + 1) % len(cycle)
                idx += 1
    

    print(*ret, sep="\n")


main()