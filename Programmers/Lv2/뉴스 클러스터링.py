"""
자카드 유사도 문제.
- 두 집합 A, B 사이의 자카드 유사도 J(A, B) = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값

1. 원래 내 풀이. Counter 모듈을 쓰지 않은 풀이.
2. Counter 모듈을 사용한 풀이.
"""

# 1
def solution(str1, str2):

    def counts(string):
        string = string.lower()
        lst = [string[i:i+2] for i in range(len(string)-1) if string[i:i+2].isalpha()]
        cnt = {}
        for key in lst:
            cnt[key] = cnt.get(key, 0) + 1
        return cnt
    
    c1, c2 = counts(str1), counts(str2)
    ss = set(c1.keys()) | set(c2.keys())
    s1 = sum(min(c1.get(key, 0), c2.get(key, 0)) for key in ss)
    s2 = sum(max(c1.get(key, 0), c2.get(key, 0)) for key in ss)

    if not s2:
        return 65536
    else:
        return int(s1 / s2 * 65536)

# 2
from collections import Counter

def solution(str1, str2):
    def divide(string):
        string = string.lower()
        return [string[i:i+2] for i in range(len(string)-1) if string[i:i+2].isalpha()]
    
    s1, s2 = divide(str1), divide(str2)
    c1, c2 = Counter(s1), Counter(s2)
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    
    if union == 0:
        return 65536
    else:
        return int(intersection / union * 65536)