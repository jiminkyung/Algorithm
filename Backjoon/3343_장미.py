# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/3343
# 참고👉 https://velog.io/@alswndit/%EB%B0%B1%EC%A4%80-3343%EB%B2%88-%EC%9E%A5%EB%AF%B8-G4

# 메모리: 32412KB / 시간: 100ms
from sys import stdin


input = stdin.readline

N, A, B, C, D = map(int, input().split())

# 효율을 A < C 로 맞춰줌
if A*D > B*C:  # 만약 A가 더 효율이 크다면 swap
    A, B, C, D = C, D, A, B

min_cost = float("inf")  # 🚨inf(1e9) 사용 X

# A꽃집에서 최소한으로 구매하고 나머지 꽃은 C꽃집에서 구매한다.
# 최소공배수(편의상 A*C만큼) 진행
for A_cnt in range(C):
    C_cnt = max(0, -(-(N - A_cnt * A) // C))  # 반올림 처리. ceil함수대신 사용.
    min_cost = min(B*A_cnt + D*C_cnt, min_cost)
    if C_cnt == 0:  # 모은 꽃의 개수가 N을 넘어가면 break
        break

print(min_cost)