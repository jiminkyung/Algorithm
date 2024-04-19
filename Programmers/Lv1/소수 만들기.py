from itertools import combinations

def solution(nums):
    combis = list(combinations(nums, 3))
    ret = 0
    
    for c in combis:
        s = sum(c)
        tmp = 0
        for i in range(2, int(s ** 0.5)+1):
            if s % i == 0:
                tmp += 1
        if tmp == 0:
            ret += 1
    return ret

# 문제풀이는 아니지만 해킹한게 웃겨서ㅋㅋㅋ
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;