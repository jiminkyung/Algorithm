# 피자좀 그만 나눠먹어라

def solution(n):
    if n % 7 == 0:
        return n // 7
    elif n < 7:
        return 1
    else:
        return n // 7 + 1

# 젠장ㅜㅜ 수학공부 열심히할걸
def solution(n):
    return (n - 1) // 7 + 1

# 수학문제집을 살까?
def solution(n):
    return -(-n//7)