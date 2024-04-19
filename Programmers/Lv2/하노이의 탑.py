# 재귀 함수 문제였다.
# 아래는 클로드 풀이...

# 이해하려면 좀 더 봐야겠다.
def hanoi(n, start, end, aux, result):
    if n == 1:
        result.append([start, end])
        return
    
    hanoi(n-1, start, aux, end, result)
    result.append([start, end])
    hanoi(n-1, aux, end, start, result)

def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result