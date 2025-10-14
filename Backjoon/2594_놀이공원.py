# 구현


# 문제: https://www.acmicpc.net/problem/2594

# 도움이 됐던 반례👉 https://www.acmicpc.net/board/view/121859
# ⭐ 현재까지 운영한 기구 중 끝나는 시간이 가장 늦은 기구를 기준으로 계산해야 함.
# 만약 1번 기구가 12:10에 끝나고, 2번 기구가 12:00에 끝난다면, 3번 기구까지의 시간을 계산할 때 1번 기구를 기준으로 삼아야 함.

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    times = [input().split() for _ in range(N)]
    times.sort()  # 시작시간 기준으로 오름차순 정렬

    rest = [0]  # 쉴 수 있는 시간들

    prev = 600  # 이전 기구 업무가 끝나는 시간 (초기값은 오픈시간인 오전 10시로 설정)

    for s, e in times:
        # 현재 기구를 운영하기 10분 전의 시간
        curr = int(s[:2]) * 60 + int(s[2:]) - 10
        
        # 짬이 난다면 쉬는시간 계산
        if curr > prev:
            rest.append(curr - prev)
        
        # 만약 이전 업무가 끝나는 시간보다 현재 업무가 끝나는 시간이 더 늦다면 prev 갱신
        if prev < int(e[:2]) * 60 + int(e[2:]) + 10:
            prev = int(e[:2]) * 60 + int(e[2:]) + 10
    else:
        # 마지막 기구 운영을 마치는 시간과 마감시간 사이 쉬는시간 계산
        last = 22 * 60

        if last > prev:
            rest.append(last - prev)
    
    print(max(rest))


main()