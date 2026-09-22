# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/77486


def solution(enroll: list[str], referral: list[str], seller: list[str], amount: list[int]) -> list[int]:
    numbers = {name: i for i, name in enumerate(enroll)}  # numbers[이름]: 해당 판매원의 인덱스
    ret = [0] * len(enroll)

    for i in range(len(seller)):
        cost = amount[i] * 100
        name = seller[i]  # i번째 판매 데이터의 판매원 이름

        # 분배금을 지급해야 할 상대가 센터일때까지 반복
        while name != "-":
            # 🚨 수익금, 분배금 계산 시 절사 처리에 주의해야함.
            # 처음엔 수익금 = int(cost * 0.9), 분배금 = int(cost * 0.1) 로 계산했으나 약간의 오차가 생김.
            # 수익금 = cost - cost // 10, 분배금 = cost // 10 와 같이 계산하거나,
            # (아래와 같이) 수익금을 따로 연산하지 않고, 절사한 분배금을 사용해서 계산하면 제대로 된 값이 나옴.
            distrib = int(cost * 0.1)
            profit = cost - distrib

            # 분배금액이 1원 미만일경우 name 판매원이 전체를 먹음
            if distrib < 1:
                ret[numbers[name]] += cost
                break

            ret[numbers[name]] += profit
            cost = distrib
            name = referral[numbers[name]]  # 분배금을 받은 판매원으로 name 갱신
        
    return ret