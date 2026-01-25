# 구현
# 그리디 알고리즘
# 정렬
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3235

# 기본적인 그리디 문제
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    K, L = map(int, input().split())
    
    times = []  # A는 0, B는 1로 기록

    # A, B에서 출발하는 배편을 분 단위로 환산해서 저장. (시간, A/B)
    for _ in range(int(input())):
        hh, mm = input().rstrip().split(":")
        t = int(hh) * 60 + int(mm)
        times.append((t, 0))
    
    for _ in range(int(input())):
        hh, mm = input().rstrip().split(":")
        t = int(hh) * 60 + int(mm)
        times.append((t, 1))
    
    ferry_A = []  # A에서 출발할 수 있는 배
    ferry_B = []  # B에서 출발할 수 있는 배
    # 어차피 이동 시간, 승선 시간은 A, B 상관없이 같으니,
    # ferry_ 에는 배가 오름차순으로 저장됨.

    times.sort()

    # 오름차순으로 탐색
    for time, town in times:
        # 배편이 A에서 출발하는 경우
        if town == 0:
            # 대기중인 배편이 있고, 현재 시간보다 첫번째 배편의 A 도착 시간이 이르거나 같다면.
            if ferry_A and ferry_A[0] <= time:
                ferry_A = ferry_A[1:]
            # A에서 출발해서 B로 도착하는 시간 계산 후 ferry_에 추가
            ferry_B.append(time + K + L)
        else:
            if ferry_B and ferry_B[0] <= time:
                ferry_B = ferry_B[1:]
            ferry_A.append(time + K + L)

    print(len(ferry_A) + len(ferry_B))


main()