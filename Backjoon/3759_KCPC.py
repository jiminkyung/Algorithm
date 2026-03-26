# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/3758
# 메모리: 32412KB / 시간: 80ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        solve()


def solve():
    # 팀의 갯수, 문제의 갯수, 내 팀 ID, 로그 엔트리 수
    n, k, t, m = map(int, input().split())

    # score[i][j]: i 팀의 j번 문제 점수
    score = [[0] * (k+1) for _ in range(n+1)]
    # team[팀 ID]: [제출 횟수, 마지막 제출 시간, 현재까지의 총 점수, 팀 ID]
    team = [[0, k+1, 0, num] for num in range(n+1)]

    # 팀 ID, 문제 번호, 점수
    for time in range(m):
        i, j, s = map(int, input().split())

        # 이전에 푼 점수보다 지금 푼 점수가 더 높다면 갱신.
        if s > score[i][j]:
            team[i][2] += s - score[i][j]  # 그냥 차이값만큼 더해주기
            score[i][j] = s
        
        team[i][0] += 1
        team[i][1] = time
    
    # (점수 높은 순, 제출 횟수 적은 순, 마지막 제출 시간이 더 빠른 순) 으로 정렬.
    team.sort(key=lambda x: (-x[2], x[0], x[1]))

    # 팀 ID가 t인 팀 찾기
    ret = next(i+1 for i, val in enumerate(team) if val[3] == t)
    print(ret)
    # for i in range(n+1):
    #     if team[i][3] == t:
    #         print(i+1)
    #         break


main()