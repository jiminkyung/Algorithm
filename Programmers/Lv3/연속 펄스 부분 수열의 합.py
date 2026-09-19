# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/161988


# 간단한 DP 문제
def solution(sequence: list[int]) -> int:
    N = len(sequence)

    # 펄스 순서별로 DP 생성 후 계산.
    # 🚨 펄스(1, -1, 1...) 생성 시 주의사항!
    # -1 ** i 또는 -1 ** (i+1)로 계산하면, -(1 ** i)로 취급됨.
    # -1 자체로 취급할 수 있도록 (-1)로 표기해야함.

    # 1. (1, -1) 순서로 곱했을때의 DP
    dp_1 = [0] * N
    s_1 = [sequence[i] * ((-1) ** i) for i in range(N)]
    dp_1[0] = s_1[0]

    for i in range(1, N):
        dp_1[i] = max(dp_1[i-1], 0) + s_1[i]  # 이전 연속 부분 수열을 이어가는게 나은지, 현재 위치에서부터 수열을 새로 생성하는게 나은지 판단.
    
    # 2. (-1, 1) 순서로 곱했을때의 DP
    dp_2 = [0] * N
    s_2 = [sequence[i] * ((-1) ** (i+1)) for i in range(N)]
    dp_2[0] = s_2[0]

    for i in range(1, N):
        dp_2[i] = max(dp_2[i-1], 0) + s_2[i]
    
    # 각 DP값의 최대값을 추출하고, 둘 중 더 큰값을 반환.
    ret = max(max(dp_1), max(dp_2))
    return ret