# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/20055

# 문제 자체를 잘못 이해했다... 맨 처음부터 로봇을 놓는게 아님. 우선 회전시킨 뒤 0번째 자리에 로봇을 두는것이었음.
# 참고👉 https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-20055-%EC%BB%A8%EB%B2%A0%EC%9D%B4%EC%96%B4-%EB%B2%A8%ED%8A%B8-%EC%9C%84%EC%9D%98-%EB%A1%9C%EB%B4%87-Python
# 위 풀이에선 deque의 rotate를 사용했는데, 슬라이싱을 사용하는게 더 빠르고 메모리 효율이 좋음.

# 메모리: 31252KB / 시간: 2660ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
robots = [False] * N

turn = 0

while A.count(0) < K:
    turn += 1

    # 컨베이어벨트 한 칸 회전.
    A = A[-1:] + A[:-1]
    robots = robots[-1:] + robots[:-1]

    # 만약 N번째 칸에 로봇이 있다면 빼냄.
    if robots[N-1]:
        robots[N-1] = False
    
    # 오래된 로봇부터 순회. 로봇을 옮길 수 있다면 옮긴 후 내구도 업데이트.
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and A[i+1] > 0:
            robots[i+1] = True
            robots[i] = False
            A[i+1] -= 1
    
    # 로봇을 옮긴 후 N번째 칸에 로봇이 존재한다면 빼냄.
    if robots[N-1]:
        robots[N-1] = False
    
    # 0번째 칸의 내구도가 1 이상이라면 로봇 추가!
    if A[0] > 0:
        robots[0] = True
        A[0] -= 1

print(turn)