# 개무식하게 풀었다. 다시는 이딴식으로 풀지 말자.
def solution(ineq, eq, n, m):
    if eq == "=":
        if ineq == ">" and (n >= m):
            return 1
        elif ineq == "<" and (n <= m):
            return 1
        else:
            return 0
    else:
        if ineq == ">" and (n > m):
            return 1
        elif ineq == "<" and (n < m):
            return 1
        else:
            return 0

# 한방 코드...ㅋ
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

# 다른버전
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1
    return answer