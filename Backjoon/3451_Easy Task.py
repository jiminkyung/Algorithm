# 구현
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/3451

# 구현, 딕셔너리 연습하기 좋은 문제
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # problems[p][team]: p문제를 시도한 team의 상태 (푸는 데 걸린 시간, 시도 횟수)
    # 만약 시도는 했으나 성공하지 못했다면 (-1, 시도 횟수) 형태로 저장됨.
    problems = {}
    # ret[i]: i 문제를 푸는데에 걸린 모든팀들의 [총 시간, 총 시도 횟수, 맞춘 팀 갯수]
    ret = [[0, 0, 0] for _ in range(9)]

    N = int(input())

    for _ in range(N):
        ss, team, p, res = input().rstrip().split()
        ss = int(ss)
        problems.setdefault(p, {})

        # 맞췄을경우
        if res == "A":
            pss, cnt = problems[p].get(team, (-1, 0))
            if pss == -1:  # 아직 맞추지 못한 상태라면 업데이트
                problems[p][team] = (ss, cnt + 1)
                p_num = ord(p) - 65
                ret[p_num][0] += ss
                ret[p_num][1] += cnt + 1
                ret[p_num][2] += 1
        # 맞추지 못했을경우
        else:
            pss, cnt = problems[p].get(team, (-1, 0))
            if pss == -1:  # 맞추지 못한 상태라면 횟수만 업데이트
                problems[p][team] = (-1, cnt + 1)
    
    for i in range(9):
        if not ret[i][2]:
            print(f"{chr(i + 65)} 0")
        else:
            ss_avg = ret[i][0] / ret[i][2]
            cnt_avg = ret[i][1] / ret[i][2]

            print(f"{chr(i + 65)} {ret[i][2]} {cnt_avg:.2f} {ss_avg:.2f}")


main()