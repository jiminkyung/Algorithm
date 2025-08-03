# 수학
# 브루트포스 알고리즘
# 백트래킹


# 문제: https://www.acmicpc.net/problem/1821

# 백트래킹, 슬라이싱 연습하기 좋은 문제...
# 메모리: 32412KB / 시간: 68ms
from sys import stdin


input = stdin.readline

def main():
    """
    파스칼의 삼각형을 이용하는 문제.
    차이점은 (기존): 위 -> 아래로 향하는 경우의 수, (문제): 아래 -> 위로 향하는 경우의 수 를 차용하는것.

    🗝️따라서 맨 윗줄의 i번째 숫자는 최종값 F에 C(N-1, i)만큼 기여하는 셈. (i가 0부터 시작한다고 가정)

    먼저 C(N-1, 0) ~ C(N-1, N-1) 계수를 구해준다.
    방법은 두가지가 있음.
        1. 홀짝성 판별해서 반만 계산 후 이어붙임
        2. 0 ~ N-1까지 쭉 계산
    N이 최대 10이기때문에 한번에 계산해도 상관없다.
    
    1. 홀짝 판별
        일단 N 홀짝성부터 검사한다.
        - N이 짝수라면?
            - ex) N = 6이면, C(5, 0) ~ C(5, 5)까지 총 6개의 계수가 나온다.
            - 따라서 정확히 반 갈라 C(5, 2)까지만 구해주면 됨. (나머지는 반전시킨다. C(n, r) = C(n, n-r) 이니까)
            - 대칭이므로 앞의 3개를 모두 뒤집어서 추가
        - N이 홀수라면?
            - ex) N = 5이면, C(4, 0) ~ C(4, 4)까지 총 5개의 계수가 나온다.
            - 중간값 C(4, 2)까지 구한 다음, 중간값 제외하고 나머지만 반전시켜야함
            - 즉, 앞의 3개 중에서 가운데 1개는 제외하고 나머지 2개만 뒤집어서 추가

        -> 일단 홀수든 짝수든 (N+1)//2 개까지는 무조건 구해야하는 상황.

        정리하면,
        - N이 짝수일 때: 모든 앞부분을 반전해서 추가 (lst[:3][::-1])
        - N이 홀수일 때: 중간값 제외하고 나머지만 반전해서 추가 (lst[:2][::-1])

        즉, lst[:(N+1)//2 - int(N % 2 != 0)][::-1] 로 계산 가능
        - N이 짝수: (N+1)//2 - 0 = (N+1)//2 개를 반전
        - N이 홀수: (N+1)//2 - 1 개를 반전
    
    ⭐굳이 홀짝 나누지 말고 그냥 N이 짝수일땐 lst[:]를, 홀수일땐 lst[:-1]을 반전시켜주면 됨.
    
    2. 0 ~ N-1까지 쭉 계산
        for문의 범위를 N으로 잡아서 쭉 돌리면 된다.

    위 조건대로 윗줄의 값을 계산하고, 그 합이 F인 경우를 백트래킹으로 찾는다.
    작은 수 부터 탐색하므로 제일 첫번째로 만족하는 경우가 답이 된다.
    """
    N, F = map(int, input().split())

    def combination(n: int, r: int):
        if r == 0 or r == n:
            return 1
        
        ret = 1
        for i in range(r):
            ret = ret * (n - i) // (i + 1)
        return ret
    

    def backtrack(pos: int, curr_sum: int, path: list):
        # 윗줄을 모두 채웠다면 합이 F가 되는지 확인.
        # 만족하면 path, 아니라면 None 반환.
        if pos == N:
            if curr_sum == F:
                return path
            return None
        
        for i in range(1, N+1):
            if i in path:
                continue
            nxt_sum = curr_sum + lst[pos] * i  # sum = num * C(n, pos-1)
            # 추가했을때의 합이 F를 초과한다면 불가능한 조합. 건너뛴다.
            if nxt_sum > F:
                continue
            ret = backtrack(pos+1, nxt_sum, path + [i])
            if ret:
                return ret
        return None
    
    
    lst = []

    # N이 3이라면? C(2, 1)까지는 구해야 한다. 즉, 1번 인덱스까지 구해야 함.
    # => 따라서 for문 순환 시 (N+1) // 2 로 지정해야함.
    for i in range((N+1) // 2):
        lst.append(combination(N-1, i))
    
    # 한줄로 하면 아래와 같음. 다만 메모리 사용량이 늘어남.
    # lst.extend(lst[:(N+1)//2 - int(N % 2 != 0)][::-1])
    if N % 2 == 0:
        lst.extend(lst[:][::-1])
    else:
        lst.extend(lst[:-1][::-1])

    ret = backtrack(0, 0, [])
    print(*ret)


main()