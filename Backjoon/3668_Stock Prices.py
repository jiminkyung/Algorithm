# 자료구조
# 우선순위 큐


# 문제: https://www.acmicpc.net/problem/3668

# 최대힙, 최소힙 사용 문제.
# 메모리: 35508KB / 시간: 76ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        ret = solve()
        print(*ret, sep="\n")


def solve() -> list[str]:
    N = int(input())

    # 매수가격은 가장 비싼 가격으로, 매도가격은 가장 싼 가격으로 선정함.
    # 매수가격 >= 매도가격 을 만족하면, 누가 먼저 요청했는지와는 상관없이 매도가격으로 구매한다.
    # 항상 최저가로 구매하는 셈.

    # buyer: 매수요청 리스트. [-가격, 주] 형식으로 최대 힙 구성.
    # seller: 매도요청 리스트. [가격, 주] 형식으로 최소 힙 구성.
    buyer = []
    seller = []
    ret = []

    # 현재 가격 (거래 발생 시 갱신)
    curr_price = "-"

    for _ in range(N):
        line = input().rstrip().split()
        share = int(line[1])
        price = int(line[-1])
        if line[0] == "buy":
            heappush(buyer, [-price, share])
        else:
            heappush(seller, [price, share])
        
        # 두 힙 모두 요청이 존재하고, 매수가 >= 매도가 조건을 만족할때까지 반복.
        while buyer and seller and (-buyer[0][0] >= seller[0][0]):
            price = seller[0][0]
            share = min(seller[0][1], buyer[0][1])  # 현재 거래할 주

            # ⭐ 만약 주(share)가 힙의 순서를 결정하는 요소였다면 pop으로 뺀 뒤 다시 push했어야함.
            # 하지만 순서 결정은 가격(price)이므로, 그냥 pop하지 않고 직접 조정해도 상관 없음.
            seller[0][1] -= share
            buyer[0][1] -= share

            # 더이상 남아있는 주가 없다면 pop
            if seller[0][1] == 0:
                heappop(seller)
            if buyer[0][1] == 0:
                heappop(buyer)
            
            # 거래 가격 갱신
            curr_price = price
        
        a = seller[0][0] if seller else "-"
        b = -buyer[0][0] if buyer else "-"
        # print(f"{a} {b} {curr_price}")
        ret.append(f"{a} {b} {curr_price}")
    
    return ret


main()