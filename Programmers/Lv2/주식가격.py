"""
효율성 3번에서 오래걸렸다.
그리고 '스택'알고리즘이라는 취지에 알맞지 않은 풀이인듯.
"""

def solution(prices):
    ret = []
    for i in range(len(prices)):
        cnt = 0
        for k in range(i+1, len(prices)):
            cnt += 1
            if prices[k] < prices[i]:
                break
        ret.append(cnt)
    return ret

# 사람들이 알맞은 풀이라고 칭찬하는 풀이.
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer