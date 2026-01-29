# 수학
# 구현
# 정렬
# 사칙연산
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3252
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    num = 1
    # 1번 선수의 기록
    time = float(input())
    min_time = time

    # 선수들의 기록을 (시간, 선수번호)로 저장
    stamps = [(time, num)]

    for _ in range(N-1):
        num += 1
        time = input().rstrip()

        if time[0] == "+":
            time = min_time + float(time[1:])
        else:
            time = min_time - float(time[1:])
        
        # 기록 추가 후 최단 시간 갱신
        stamps.append((time, num))
        min_time = min(time, min_time)
    
    # 오름차순으로 정렬 후 M등부터 1등까지 선수 번호 저장
    stamps.sort()
    second = [num for _, num in stamps[:M][::-1]]

    # M등 선수의 새로운 기록
    time = float(input())
    min_time = time

    # 마찬가지로 (시간, 선수번호)로 저장
    stamps = [(time, second[0])]

    for i in range(1, M):
        num = second[i]
        time = input().rstrip()

        if time[0] == "+":
            time = min_time + float(time[1:])
        else:
            time = min_time - float(time[1:])
        
        stamps.append((time, num))
        min_time = min(time, min_time)
    
    # 3등까지 추출
    stamps.sort()
    ret = [stamps[i][1] for i in range(3)]

    print(*ret, sep="\n")


main()