def solution(s1, s2):
    return len(set(s1) & set(s2))

# set 교집합
# 1. set1 & set2
# 2. set1.intersection(set2)