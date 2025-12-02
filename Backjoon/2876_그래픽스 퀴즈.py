# 구현
# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2876

# DP로 분류된 문제인데 그냥 풀었음.
# 메모리: 41144KB / 시간: 112ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    # 마지막 학생까지 체크하기 위해 빈 값 (0, 0) 추가.
    arr = [tuple(map(int, input().split())) for _ in range(N)] + [(0, 0)]

    ret = (0, 0)  # (최대 학생 수, 등급)
    
    # 작은 등급부터 확인
    for g in range(1, 6):
        # cnt: g등급으로 채점할 수 있는 연속 학생 수
        # max_cnt: g등급으로 채점할 수 있는 최대 연속 학생 수
        cnt = max_cnt = 0
        for a, b in arr:
            if a == g or b == g:
                cnt += 1
            else:
                # 연속이 아니라면 max_cnt 값 비교, cnt 리셋.
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0
        # 이전 등급의 최댓값보다 크다면 갱신시켜줌.
        if max_cnt > ret[0]:
            ret = (max_cnt, g)
    
    print(*ret)


main()