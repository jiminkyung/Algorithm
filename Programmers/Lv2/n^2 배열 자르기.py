"""
규칙을 찾아내서 풀어야하는 문제.
- 행과 열의 값 중 더 큰것을 값으로 한다.

문제 설명 순서대로 무식하게 풀면 시간초과다.
아예 처음부터 left, right만큼만의 리스트를 생성해야 통과할 수 있다.
"""

# 첫번째 시도... 시간초과!!!
def solution(n, left, right) -> list:
    arr = [[0]*n for _ in range(n)]
    
    num = 1
    while num <= n:
        for i in range(num):
            arr[i][num-1] = num
            arr[num-1][i] = num
        num += 1

    new_arr = [n for row in arr for n in row]
    
    return new_arr[left:right+1]

# 두번째 시도~! 규칙을 찾아내서 최대한 심플하게... => 이것도 시간초과.
def solution(n, left, right) -> list:
    arr = [max(i, k) for i in range(1, n+1) for k in range(1, n+1)]
    return arr[left:right+1]

# 세번째 시도. 처음부터 left, right을 공략하는 방식. => 통과!
def solution(n, left, right) -> list:
    """
    left부터 right+1 까지 i로 순회한다.
    행: i//n, 열: i%n 으로 구할 수 있다.
    max(행, 열)로 둘중 더 큰값을 구하고 1을 더해 append한다.(문제에서의 i는 1부터 n까지이기 때문이다.)
    """
    ret = []

    for i in range(left, right+1):
        row, col = i//n, i%n
        ret.append(max(row, col) + 1) # 문제의 i는 1부터이므로
    return ret