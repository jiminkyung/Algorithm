# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/2457

# 참고: https://velog.io/@minjungh63/Python-%EB%B0%B1%EC%A4%80-2457%EB%B2%88-%EA%B3%B5%EC%A3%BC%EB%8B%98%EC%9D%98-%EC%A0%95%EC%9B%90
# 메모리: 41384KB / 시간: 224ms
from sys import stdin


input = stdin.readline

N = int(input())
flowers = sorted(tuple(map(int, input().split())) for _ in range(N))
ret = 0

# 꽃이 지는 날짜 (초기값: 3월 1일)
end = (3, 1)
i = 0

while i < N:
    m1, d1, m2, d2 = flowers[i]
    latest = 0

    # 현재 꽃이 피는날 <= end < 지는날이면 현재 꽃을 심을 수 있음.
    if (m1, d1) <= end < (m2, d2):
        latest = (m2, d2)

        # 위 조건하에 가장 늦게 지는 꽃을 찾기
        while i < N-1:
            m1, d1, m2, d2 = flowers[i+1]
            if (m1, d1) > end:  # 꽃이 피는날짜가 end보다 늦다면 탐색 종료
                break
            if (m2, d2) > latest:
                latest = (m2, d2)
            i += 1

        end = latest
        ret += 1

        # 꽃이 지는 날짜가 11월 30일보다 늦다면 출력 후 종료. (실제 꽃이 지는날은 (지는날 - 1)이기 때문에 같거나 작으면 안됨.)
        if latest > (11, 30):
            print(ret)
            break
    i += 1
else:
    # break없이 빠져나올경우 (꽃이 지는 날짜가 11월 30일을 못넘길경우)
    print(0)