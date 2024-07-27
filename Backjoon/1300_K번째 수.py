# 이분 탐색

# 메모리: 31120KB / 시간: 764ms

"""
인덱스는 1부터 시작한다.
1부터 N*N까지가 범위가 됨.
범위 사이의 수 target보다 작은 숫자의 갯수를 체크해가며 범위를 변경하는 방식.
"""

N = int(input())
k = int(input())

def counting(x, n):
    """
    숫자 x보다 작은 수의 갯수 = cnt
    배열은 [1, 2, 3], [2, 4, 6]... 이런식으로 각 행은 그 행의 배수로 이루어져있음.
    즉 각 행에서 x보다 작은 수 = x를 i로 나눈 몫인 셈이다.
    하지만 N*N배열이기 때문에 갯수가 N보다 클 순 없으므로 min()으로 체크해줘야한다.
    """
    cnt = 0
    for i in range(1, n+1):
        cnt += min(x // i, n)
    return cnt

def binary_search(n, target):
    """
    start == end가 되는 순간 종료.
    만약 target값보다 작다면 시작값을 mid+1로 재설정.
    아니라면(target값보다 크거나 같다면) 종료값을 mid로 재설정. mid가 답일수도 있으므로 mid-1이 아닌 mid로 설정해준다.
    """
    start, end = 1, n*n

    while start < end:
        mid = (start + end) // 2
        
        if counting(mid, n) < target:
            start = mid + 1
        else:
            end = mid
    
    return start

print(binary_search(N, k))