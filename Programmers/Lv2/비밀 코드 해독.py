# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/388352

from itertools import combinations


def solution(n: int, q: list[list[int]], ans: list[int]) -> int:

    def check(comb: tuple[int]):
        """ 해당 조합이 암호 조건에 부합하는지 확인 """
        for i in range(len(q)):
            cnt = 0
            for j in range(5):
                cnt += comb.count(q[i][j])

            if cnt != ans[i]:
                return 0
        return 1
    

    ret = 0

    for comb in combinations(range(1, n+1), 5):
        ret += check(comb)
    
    return ret