# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2891
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # 팀 수, 카약 손상 팀 수, 여분 카약 수
    N, S, R = map(int, input().split())

    # 손상 팀, 여분 카약 보유 팀을 set으로 저장
    ruined = set(map(int, input().split()))
    spare = set(map(int, input().split()))

    # 여분 카약이 있으나 손상된 팀은 배제시킴.
    both = ruined & spare
    ruined -= both
    spare -= both

    # 손상 팀 기준으로 체크
    ruined = sorted(ruined)
    cnt = len(ruined)  # 출발 불가 팀 수

    # 현재 팀 기준 -1, +1 순서로 해당 팀이 여분 카약을 갖고 있는지 체크.
    # 갖고 있다면 카운트 -1 처리 후 해당 팀을 여분 카약 팀에서 제외.
    for r in ruined:
        if r-1 in spare:
            spare -= {r-1}
            cnt -= 1
        elif r+1 in spare:
            spare -= {r+1}
            cnt -= 1
    
    print(cnt)


main()