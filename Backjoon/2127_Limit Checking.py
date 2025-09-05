# 구현
# 시뮬레이션
# 자료 구조
# 문자열
# 집합과 맵  # 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/2127

# 🚨최대/일일 둘 다 초과시 출력형식 주의!!! https://www.acmicpc.net/board/view/140620
# 오랜만에 푸는 긴 구현 문제~ 재밌었음. 나중에 다시 풀어볼만 함.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # customers[name]: name 고객의 한도와 계좌. dict[dict[list]] 형태로 저장.
    # customers[name]["accounts"]: 계좌, customers[name]["limits"]: 한도.
    customers = {}

    # curr[date][name]: date 날짜, name 고객의 한도 상황. 마찬가지로 dict[dict[list]] 형태.
    curr = {}

    turn = 1

    def check(data: list, customers: dict[dict[list]]) -> str:
        nonlocal curr
        # 날짜, 이름, 출금계좌, 금액, 입금계좌
        date, name, source, amount, destination = data

        # 출금계좌가 본인 소유가 아닐경우
        if source not in customers[name]["accounts"]:
            return "NOT OWNER"
        
        date = date[:8]
        amount = float(amount)

        # lim: 고객의 현재 한도 상황을 보여주는 리스트.
        # -> [IAT 최대 지시 한도, IAT 일일 노출 한도 중 남은양, 일반결제 최대 지시 한도, 일반결제 일일 노출 한도 중 남은양]
        # curr에 date 키가 없다면 빈 딕셔너리 생성 -> date에 name 키가 없다면 고객의 한도 데이터를 가져온다.
        lim = curr.setdefault(date, {}).setdefault(name, customers[name]["limits"][:])
        
        # 입금계좌가 본인 소유라면 IAT 결제
        if destination in customers[name]["accounts"]:
            IAT_MAX = bool(lim[0] < amount)        # 최대 지시 한도 초과시 True
            IAT_DEL = bool(lim[1] - amount < 0.0)  # 일일 노출 한도 초과시 True

            # 🚨지시 한도와 일일 노출 한도를 모두 추가하면 "ㅇㅇ MAX EXCEEDED"로 출력해야함. 문제 설명이 이상하다.
            # 1. IAT_MAX, IAT_DEL이 모두 True
            if IAT_MAX:
                return "IAT MAX EXCEEDED"
            # 2. IAD_DEL만 True
            elif IAT_DEL:
                return "IAT DEL EXCEEDED"
            # 3. 출금 가능
            else:
                curr[date][name][1] -= amount
                return "IAT OK"
        # 아니라면 일반 결제
        else:
            PAY_MAX = bool(lim[2] < amount)        # 최대 지시 한도 초과시 True
            PAY_DEL = bool(lim[3] - amount < 0.0)  # 일일 노출 한도 초과시 True

            if PAY_MAX:
                return "PAYMENT MAX EXCEEDED"
            elif PAY_DEL:
                return "PAYMENT DEL EXCEEDED"
            else:
                curr[date][name][3] -= amount
                return "PAYMENT OK"


    while True:
        data = input().rstrip().split(",")

        # 1. 고객 생성 후 한도 저장
        if data[0] == "1":
            name, *limit = data[1:]
            customers[name] = {"limits": [], "accounts": []}
            limit = list(map(float, limit))
            # limit: IAT 최대 지시 한도, IAT 일일 노출 한도, 일반 지불 최대 지시 한도, 일반 지불 일일 노출 한도
            customers[name]["limits"].extend(limit)
        # 2. 고객 계좌 추가
        elif data[0] == "2":
            name, account = data[1:]
            customers[name]["accounts"].append(account)
        # 3. 입출금 처리
        elif data[0] == "5":           
            ret = check(data[1:], customers)
            print(f"INSTRUCTION {turn}: {ret}")
            turn += 1
        else:
            break


main()