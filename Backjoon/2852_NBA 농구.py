# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/2852
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    score = [0, 0]  # 점수 상황
    stamp = 0  # 직전 분기점
    total = [0, 0]  # 누적 우승 시간

    for _ in range(N):
        team, time = input().rstrip().split()
        team = int(team) - 1
        mm, ss = map(int, time.split(":"))
        time = mm * 60 + ss  # 분으로 변환
        
        # 동점일경우 분기점 저장 후 현재 팀에 점수 추가
        if score[0] == score[1]:
            stamp = time
            score[team] += 1
            continue

        # 아니라면 이기고 있는 팀 파악
        winning_team = int(score[0] < score[1])

        # 직전까지 이기고 있던 팀에 우승 시간 추가, 분기점 저장
        total[winning_team] += time - stamp
        stamp = time
        # 현재 우승 팀에 점수 추가
        score[team] += 1
    else:
        # 🚨마지막에 동점일수도 있음. 동점이 아니라면 이기고 있던 팀에 남은 시간 추가.
        if score[0] != score[1]:
            winning_team = int(score[0] < score[1])
            total[winning_team] += (48 * 60) - stamp
    
    for time in total:
        mm, ss = time // 60, time % 60
        print(f"{mm:0>2}:{ss:0>2}")  # 0>2: 두자릿수에 맞춰 0 삽입


main()