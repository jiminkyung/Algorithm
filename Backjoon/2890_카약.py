# 구현
# 문자열
# 정렬


# 문제: https://www.acmicpc.net/problem/2890
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    score = {}  # 위치별로 팀 저장

    for _ in range(R):
        data = input().rstrip()
        for i in range(C-2, 0, -1):  # F 건너뛰고 체크 시작
            if data[i] != ".":  # 숫자로 이루어졌다면 팀 체크
                team = int(data[i])
                score.setdefault(i, []).append(team)
                break
    
    # 위치 기준으로 내림차순 정렬 (위치값이 큰 팀 = 결승선과 가까운 팀)
    rank = sorted(score.items(), reverse=True)
    ret = [0] * 9
    for i, (key, val) in enumerate(rank):
        for team in val:
            ret[team-1] = i+1  # 등수 저장
    
    print(*ret, sep="\n")


main()