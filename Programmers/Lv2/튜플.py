"""
s는 집합이 담긴 문자열.
중괄호({, })를 제거해준 뒤 콤마를 기준으로 나눠준다.
set으로 중복을 제거 후 각 원소를 count, 내림차순으로 sort.
각 요소는 (원소, 횟수)의 형태, 리스트 컴프리헨션을 통해 원소를 int형으로 변환 후 반환.
"""

def solution(s: str) -> list:
    s = s.replace("{", "").replace("}", "")
    nums = s.split(",")
    nums_set = set(nums)
    counts = [(n, nums.count(n)) for n in nums_set]
    counts.sort(key=lambda x: x[1], reverse=True)
    return [int(n[0]) for n in counts]

# 모듈을 이용한 풀이 발견. Counter와 re 사용.
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter