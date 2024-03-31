# 1차시도 => 순열 => X
# 찾아보니 점화식을 사용하는것이 주 풀이방법이었다.

def solution(n):
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, (a+b) % 1234567
    return b