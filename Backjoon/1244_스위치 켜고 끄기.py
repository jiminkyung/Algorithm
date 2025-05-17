# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1244
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    states = list(map(int, input().split()))
    S = int(input())
    students = [tuple(map(int, input().split())) for _ in range(S)]

    # 1. 순서대로 (성별, 번호) 체크
    for gender, number in students:
        # 2-1. 남자일경우
        if gender == 1:
            # 학생 번호부터 N까지 배수에 해당되는 스위치를 toggle
            for switch_num in range(number-1, N, number):
                states[switch_num] ^= 1
        # 2-2. 여자일경우
        else:
            min_size = min(number-1, N-number)  # 체크할 수 있는 최대 범위
            max_size = 0  # 찾은 최대 구간
            pos = number-1  # 현재 번호
            # 양쪽으로 한 칸씩 이동하며 데칼코마니인지 확인
            # 맞다면 max_size 갱신, 아니라면 break
            for size in range(min_size+1):
                if states[pos-size] != states[pos+size]:
                    break
                max_size = size
            
            # 현재 번호와 max_size 구간 내에 있는 모든 스위치 toggle
            states[pos] ^= 1

            for size in range(max_size+1):
                states[pos-size] ^= 1
                states[pos+size] ^= 1
    

    # 3. 20개씩 출력
    cnt = 0

    while cnt < N:
        print(*states[cnt:cnt+20])
        cnt += 20


main()