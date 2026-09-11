# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12971


# 처음에는 DFS + 메모이제이션으로 접근했으나 시간초과.
# 🗝️ 선형 DP로 바꿔서 풀어야 함.
# -> 첫번째 스티커를 뗄 경우 / 뗴지 않을 경우로 나누어서 각각 최댓값을 구한 후, 마지막으로 둘 중 더 큰 값을 최종값으로 결정.
def solution(sticker: list[int]) -> int:
    N = len(sticker)
    first = last = 0

    # 만약 스티커가 총 세장 이하라면, 가장 큰 값을 바로 반환
    if N <= 3:
        return max(sticker)

    # 1. 첫번째(0번) 스티커를 뗄 경우 (1번째 스티커, 마지막 N-1번쨰 스티커는 사용 불가)
    # dp[i]: i번 스티커까지 살펴봤을때 얻을 수 있는 최대 점수
    dp = [0] * N
    dp[0] = dp[1] = sticker[0]  # 1번째 스티커는 사용할 수 없으니 0번째 스티커 값으로 저장

    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    first = max(dp)

    # 2. 마지막(N-1번) 스티커를 뗼 경우 (0번째 스티커, N-2번째 스티커를 사용 불가)
    dp = [0] * N
    dp[1] = sticker[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    last = max(dp)

    return max(first, last)