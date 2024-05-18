"""
<롤케이크 자르기> 문제와 비슷하게 풂.
wanted: 구매자가 원하는 상품과 갯수를 담은 딕셔너리
cnt: 조건을 만족하는 경우의 수

첫날부터 (마지막날-10)날까지 반복한다.
조건에 맞으면 바로 반환 X, 맞는 경우의 수를 구하는 문제이므로 -> 매번 products 생성(wanted 카피본)
해당 날짜로부터 10일간 체크한 후 products가 비어있는 상태라면 조건 만족 -> cnt 추가.
"""

def solution(want: list, number: list, discount: list) -> int:
    wanted = {want[i]: number[i] for i in range(len(number))}
    cnt = 0

    i = 0
    while i <= len(discount)-10:
        products = wanted.copy()

        for k in range(i, i+10):
            products[discount[k]] = products.get(discount[k], 0) - 1

            if products[discount[k]] == 0:
                del products[discount[k]]
            if not products:
                cnt += 1
        i += 1

    return cnt