def solution(l, r):
    arr = [i for i in range(l, r+1) if not set(str(i)) - {'0', '5'}]
    return arr if arr else [-1]

# 기발한 코드;; 생각해보자...
def solution(l, r):
    answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer