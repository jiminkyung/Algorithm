# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product


def solution(users: list[list[int]], emoticons: list[int]) -> list[int]:

    def calc(comb: tuple[int]) -> tuple[int, int]:
        p = c = 0

        for rate, maximum in users:
            cost = 0  # 현재 고객이 지불해야할 총 금액
            for i in range(len(comb)):
                # 할인률이 고객 예상보다 낮다면 쓰루
                if rate > comb[i]:
                    continue

                cost += emoticons[i] * (100 - comb[i]) // 100
            
            # 고객의 총 금액이 이모티콘 플러스 가입 상한인지 판단.
            if maximum <= cost:
                p += 1
            else:
                c += cost
        return p, c
    

    max_p = max_c = 0

    # 중복순열을 사용해야함. -> 중복조합 X (10, 40), (40, 10) 모두 확인해야하므로...
    for comb in product([10, 20, 30, 40], repeat=len(emoticons)):
        p, c = calc(comb)

        # 1. 플러스 가입자 수를 더 늘릴 수 있는경우.
        if max_p < p:
            max_p, max_c = p, c
        # 2. 가입 수는 같으나 판매액이 늘어나는경우.
        elif max_p == p and max_c <= c:
            max_c = c
    
    return [max_p, max_c]