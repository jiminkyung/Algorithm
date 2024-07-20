# 그리디 알고리즘

# 참고: https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-13305%EB%B2%88-%EC%A3%BC%EC%9C%A0%EC%86%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 문제를 제대로 읽자... n리터당 1원이 아니라 1리터당 n원이다.

# 메모리: 46236KB / 시간: 116ms

from sys import stdin


input = stdin.readline
N = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = float("inf")
ret = 0

for i in range(N-1):
    if min_price > price[i]:
        min_price = price[i]
    
    ret += min_price * km[i]

print(ret)


# 실행시간 1위 코드. price 리스트의 값을 각 인덱스까지의 값 중 가장 작은 값으로 재할당함.
# price[i] * km[i]
def filter_oil_price_list(N, oil_price_list:list):
    min_val = float('inf')
    for i in range(N):
        if oil_price_list[i] < min_val:
            min_val = oil_price_list[i]
        else:
            oil_price_list[i] = min_val
    return oil_price_list


def main():
    N = int(input())
    dist_list = list(map(int, input().split()))
    oil_price_list = list(map(int, input().split()))
    oil_price_list = filter_oil_price_list(N, oil_price_list)

    answer = sum([dist_list[i]* oil_price_list[i] for i in range(N-1)])
    print(answer)

if __name__ == "__main__":
    main()