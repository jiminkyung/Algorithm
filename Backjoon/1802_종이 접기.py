# 분할 정복
# 재귀


# 문제: https://www.acmicpc.net/problem/1802

# 종이접기 규칙을 이해하면 쉬운 문제. 재귀 연습할때 다시 풀어볼만한 문제~
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    종이접기 특성 상 중심을 기준으로 좌우가 반대 방향으로 꺾임.
    => 대칭적이고 재귀적인 구조

    따라서
    1. 종이의 가운데를 기준으로 왼쪽과 reverse(오른쪽)이 일치하는지,
    2. 왼쪽, 오른쪽 부분을 재귀로 넘겼을때 1번 조건을 만족하는지,
    위 과정을 종이의 길이가 1이 될 때까지 반복하면 된다. 길이가 1인 종이는 무조건 True로 반환.
    """
    def dfs(curr: str) -> bool:
        # 길이가 1이라면 True 반환
        if len(curr) == 1:
            return True
        
        mid = len(curr) // 2
        left = curr[:mid]
        right = curr[mid+1:]

        # 종이의 왼쪽 != reverse(오른쪽) 이라면 False 반환
        for i in range(mid):
            if left[i] == right[-(i+1)]:
                return False
        # 위 조건을 통과했다면 왼쪽, 오른쪽을 재귀로 넘겨 True/False 반환
        return dfs(left) and dfs(right)


    T = int(input())

    for _ in range(T):
        N = input().rstrip()
        print("YES" if dfs(N) else "NO")


main()