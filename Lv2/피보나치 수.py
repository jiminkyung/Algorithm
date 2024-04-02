# 이게 먼저 나왔어야되는거 아닌가? 왜 dp문제를 앞에...
def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a+b) % 1234567
    return a