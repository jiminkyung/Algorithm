from itertools import combinations

def solution(number):
    return sum(not sum(n) for n in combinations(number, 3))


# 더 직관적인 답. 개인적으로 더 마음에 든다.
def solution(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                # print(number[i],number[j],number[k])
                if number[i]+number[j]+number[k] == 0:
                    answer += 1           
    return answer