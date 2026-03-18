# 그리디 알고리즘
# 정렬


# 문제: https://www.acmicpc.net/problem/3603
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    n, t = map(int, input().split())
    # 돼지 번호는 1번부터 매기기
    pigs = list((d, i) for i, d in enumerate(map(int, input().split()), start=1))
    dist = list(map(int, input().split()))
    price = list(map(int, input().split()))

    cand = []

    # 특정 돼지 i를 마을 j에서 팔았을때의 순이익은 다음과 같음.
    # w = 돼지 무게, p = j마을에서의 가격, d = j마을까지의 거리, t = 연료 단가
    # w * p - w * d * t (무게i * 가격j - 무게i * 거리j * 연료단가)
    # => w * (p - d * t)

    # 🗝️ 그러므로, 최대 이익을 보려면 (p - d * t)값이 큰 마을부터 무거운 돼지를 매치시켜야함.
    for i in range(n):
        cand.append((price[i] - dist[i] * t, i))
    
    cand.sort()
    pigs.sort()

    # 결과값은 마을 0 ~ n 순으로, 각 마을에서 어떤 돼지를 팔아야하는지 출력.
    ret = [0] * n
    for i in range(n):
        _, m = cand[i]
        _, p = pigs[i]
        ret[m] = p  # m번째 마을에서 p번째 돼지 판매
    
    print(*ret)


main()