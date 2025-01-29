# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/16986

# 재귀 or permutations 사용
# 메모리: 32544KB / 시간: 604ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]


# 경희과 민호의 손동작을 0-based로 저장
hee = list(map(lambda x: int(x)-1, input().split()))
minho = list(map(lambda x: int(x)-1, input().split()))

# 세명의 손동작들을 기록
hand = [[0] * 20 for _ in range(3)]
hand[1] = hee
hand[2] = minho

# 지우가 해당 손동작을 사용했는지 체크
used = [False] * N

score = [0, 0, 0]  # 세명의 점수
idx = [0, 0, 0]  # 세명의 손동작 순서

def rsp(p1, p2) -> bool:
    if score[0] == K:  # 지우의 점수가 K에 도달한경우
        return True
    if score[1] == K or score[2] == K:  # 다른 사람이 먼저 K점까지 도달하면 실패
        return False
    if idx[0] == N:  # 또는 지우가 N개의 손동작을 모두 사용했다면 실패
        return False
    
    if p1 > p2:
        p1, p2 = p2, p1
    
    p3 = 3 - (p1 + p2)  # p3: 승자와 붙을 다음 선수

    # p1이 지우인경우
    if p1 == 0:
        # N개의 손동작 중 사용하지 않은 손동작 탐색
        for i in range(N):
            if used[i]:
                continue

            used[i] = True
            hand[0][idx[0]] = i  # 해당 손동작 사용

            hand1 = hand[p1][idx[p1]]  # 선수1의 손동작
            hand2 = hand[p2][idx[p2]]  # 선수2의 손동작

            # 값이 2라면 p1이 승자, 아니라면 p2가 승자
            winner = p1 if A[hand1][hand2] == 2 else p2
            
            score[winner] += 1
            idx[p1] += 1
            idx[p2] += 1

            if rsp(winner, p3):  # 재귀 결과가 True라면 바로 True 반환
                return True
            
            score[winner] -= 1
            idx[p1] -= 1
            idx[p2] -= 1
            
            used[i] = False
        return False
    # p1이 지우가 아닌 경우
    else:
        hand1 = hand[p1][idx[p1]]
        hand2 = hand[p2][idx[p2]]
        winner = p1 if A[hand1][hand2] == 2 else p2

        score[winner] += 1
        idx[p1] += 1
        idx[p2] += 1
        ret = rsp(winner, p3)
        score[winner] -= 1
        idx[p1] -= 1
        idx[p2] -= 1
        return ret


print(int(rsp(0, 1)))  # 지우와 경희부터 매치