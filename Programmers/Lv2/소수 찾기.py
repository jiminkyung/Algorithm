"""
itertools 모듈을 사용하면 쉽게 해결가능한 문제.
1. itertools 안쓰고 해보기
2. 사용하기
"""

# 1. TC 5, 8 시간초과.
def solution(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True
    
    ret = 0

    numbers = sorted(numbers, reverse=True)
    num_cnt = {n: numbers.count(n) for n in set(numbers)}

    for i in range(int(numbers[-1]), int("".join(numbers))+1):
        if is_prime(i):
            i_numbers = sorted(str(i), reverse=True)
            i_cnt = {i_num: i_numbers.count(i_num) for i_num in i_numbers}
            for num in i_numbers:
                if num not in num_cnt or i_cnt[num] > num_cnt[num]:
                    break
            else:
                ret += 1
    return ret

# 2
from itertools import permutations


def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            num_set.add(int("".join(num)))
    
    ret = 0

    for num in num_set:
        if is_prime(num):
            ret += 1
    
    return ret