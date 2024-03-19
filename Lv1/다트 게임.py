# 이 문제를 어디서 봤나 했더니 정규표현식 실습할때 ㅎㅎ
# https://colab.research.google.com/drive/1L87Nl1nlPJzQoF5hFvDKqV7hS-tR-llV?usp=sharing
# 일부러 정규표현식을 쓰지 않고 풀어봤다.
def solution(dartResult):
    num = ""
    ret = []
    for d in dartResult:
        if d.isdigit():
            num += d
        else:
            if num:
                ret.append(int(num))
                num = ""
            if d == "T": ret[-1] **= 3
            elif d == "D": ret[-1] **= 2
            elif d == "S": ret[-1] **= 1
            elif d == "#": ret[-1] *= (-1)
            else:
                if len(ret) > 1:
                    ret[-2] *= 2
                ret[-1] *= 2
    return sum(ret)

# 정규표현식을 쓰신 분의 코드... 보기엔 훨씬 깔끔하다.
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 난 이게 제일 멋진것같다.
def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)