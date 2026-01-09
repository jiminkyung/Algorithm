# 구현


# 문제: https://www.acmicpc.net/problem/3161

# izbori는 크로아티아어로, 한국어로는 "선거" 라고 함. 신기~
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    M, N = map(int, input().split())
    votes = [[-1] * (N+1) for _ in range(M)]

    # votes[i][j]: i번째 턴에서 j번 후보의 득표수
    for turn in range(M):
        for i, d in enumerate(map(int, input().split())):
            votes[turn][d] = i
    
    score = [0] * (N+1)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            cnt = sum(votes[k][i] < votes[k][j] for k in range(M))

            # cnt: i가 j보다 높은 순위로 뽑힌경우
            # cnt가 M//2 이하라면? j가 더 높게 뽑힌 경우가 많은거임.
            if cnt <= M // 2:
                score[j] += 1
            else:
                score[i] += 1
    
    max_score = max(score)
    ret = [i for i in range(1, N+1) if score[i] == max_score]

    print(*ret, sep="\n")


main()