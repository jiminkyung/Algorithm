# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1476


# 6064_카잉 달력과 비슷한 문제다.
# 시간초과에 주의해야한다!!!

# 메모리: 32412KB / 시간: 32ms
def finding(E, S, M):
    # 범위의 최소 공배수: 15, 28, 19
    E -= 1
    S -= 1
    M -= 1
    for year in range(E, 7980, 15):  # 15의 배수로 제한
        if year % 28 == S and year % 19 == M:
            return year + 1

E, S, M = map(int, input().split())
print(finding(E, S, M))