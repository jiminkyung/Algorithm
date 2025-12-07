# 구현
# 브루트포스 알고리즘
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/2915
# 메모리: 32412KB / 시간: 36ms
from sys import stdin
from itertools import permutations


input = stdin.readline

def main():
    units = {alp: i+1 for i, alp in enumerate(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"])}
    tens = {alp: (i+1)*10 for i, alp in enumerate(["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"])}

    rome = input().rstrip()
    L = len(rome)
    min_ret = 100  # 가장 작은 수 조합일때의 값
    ret = None  # 가장 작은 수 조합

    for perm in permutations(list(rome), L):
        word = "".join(perm)
        # word 자체가 일의 자리 또는 십의 자리의 문자일경우 해당 값 저장 (없으면 100으로)
        min_sum = units.get(word, 100)
        min_sum = min(min_sum, tens.get(word, 100))

        for i in range(1, L):
            # 둘로 쪼개서 앞은 십의 자리, 뒤는 일의 자리로 계산
            ten, unit = word[:i], word[i:]
            curr_sum = tens.get(ten, 100) + units.get(unit, 100)
            # 변환한 값이 word 조합의 최솟값보다 작다면 갱신
            if curr_sum < min_sum:
                min_sum = curr_sum
        
        # word 조합의 최솟값이 전체의 최솟값보다 작다면 갱신, 조합 저장
        if min_sum < min_ret:
            min_ret = min_sum
            ret = word
    
    print(ret)


main()