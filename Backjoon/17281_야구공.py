# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17281

# 다른 풀이를 참고했다... 까딱하면 PyPy3로도 시간초과가 나는 문제다.
# 참고👉 https://edder773.tistory.com/60

# 참고로 홈루(base)를 변수 3개 대신 리스트로 관리하면 시간초과난다.
# ⭐ 원래는 game 함수를 따로 만들어서 매 조합마다 실행했었으나 아래처럼 for문으로 실행하는게 훨씬 빠름.
# PyPy3로 통과 - 메모리: 110728KB / 시간: 672ms
from sys import stdin
from itertools import permutations


input = stdin.readline

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
max_score = 0


for perm in permutations(range(1, 9)):
    perm = list(perm)
    batter = perm[:3] + [0] + perm[3:]
    order, score = 0, 0
    for i in range(N):
        # ⭐ 가지치기
        # 만약 최고 점수 >= 현재 점수 + 앞으로 얻을 수 있는 최고점수라면 바로 return
        # (N-i): 앞으로 남은 이닝 수, 24: 한 이닝당 최소 한명은 아웃인걸 가정했을때의 최대 턴 수
        if max_score >= score + (N-i) * 24:
            break
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            curr = innings[i][batter[order]]
            if curr == 0:
                out += 1
            elif curr == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif curr == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif curr == 3:
                score += b3 + b2 + b1
                b1, b2, b3 = 0, 0, 1
            else:
                score += b3 + b2 + b1 + 1
                b1, b2, b3 = 0, 0, 0
            order = (order + 1) % 9

    max_score = max(score, max_score)
print(max_score)