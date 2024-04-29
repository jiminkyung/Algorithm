"""
해시 문제.

각 타입별로 딕셔너리화 시켜줌.
reduce 모듈을 이용해서 각 타입별 경우의 수를 곱셈.
- y + 1 => y(입는경우) +1(입지않는경우)
마지막 -1은 아무것도 안입는경우를 제하기 위함임.
"""

from functools import reduce


def solution(clothes):
    cases = {}
    for _, type in clothes:
        cases[type] = cases.get(type, 0) + 1
    
    ret = reduce(lambda x, y: x * (y + 1), cases.values(), 1) - 1
    return ret