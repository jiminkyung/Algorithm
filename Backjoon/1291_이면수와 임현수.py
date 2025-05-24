# 구현
# 많은 조건 분기
# 소인수분해


# 문제: https://www.acmicpc.net/problem/1291

# 스토리가 대단한 문제... 다 읽으면 안됨.
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    # 이면수 조건: 2, 3 합으로 만들어지는 수(사실상 5를 제외한 4 이상의 수), 자릿수의 합이 홀수
    # 임현수 조건: 합성수, 소인수 갯수가 짝수 or 2 이거나 4

    N = input().rstrip()

    def check_1(num: str):
        """ 이면수 체크 """
        if int(num) < 4 or int(num) == 5:
            return False
            
        if 4 < int(num) and sum(map(int, num)) % 2 != 0:
            return True
        return False
    
    def check_2(num: int):
        """ 임현수 체크 """
        if num == 2 or num == 4:
            return True
        
        factors = set()
        x = 2

        while x <= int(num**0.5):
            if num % x == 0:
                factors.add(x)
                num //= x
            else:
                x += 1
        
        if num > 1:
            factors.add(num)

        # 합성수(소수 X)이고 소인수의 갯수가 짝수라면 True 반환
        if len(factors) > 1 and len(factors) % 2 == 0:
            return True
        return False
    

    if int(N) == 1:
        print(3)
    else:
        # xy: 이면수 체크 결과 x, 임현수 체크 결과 y 라고 할때,
        # 00: 3, 01: 2, 10: 1, 11: 4
        ret = (check_1(N) << 1) + check_2(int(N))
        print([3, 2, 1, 4][ret])


main()