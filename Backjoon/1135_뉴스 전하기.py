# 그리디 알고리즘
# 다이나믹 프로그래밍
# 깊이 우선 탐색 (DFS)


# 문제: https://www.acmicpc.net/problem/1135

# 각 상사는 자신의 직속 부하들에게 한 명씩 전화를 걸어 뉴스를 전달함.
# 통화 시간은 1분, 동시에 여러명에게 전화를 돌릴수는 없다.
# 부하들도 뉴스를 받은 직후 자신의 부하들에게 전달하기 시작.
# => 딸린 부하들이 가장 많은 직속 부하에게 먼저 전달해야 유리함.
# => 따라서 직속부하가 그 부하들에게 전달하는 시간들을 구하고 내림차순으로 정렬.
# => 정렬된 기준으로 통화시간 (1 + a) + (직속부하가 부하들에게 전달하는 시간)을 구한다.
# => 예를들어 [4, 7, 5]라면, (1 + 7), (2 + 5), (3 + 4) 중 가장 오래 걸리는 시간을 구함.
# => 이 값이 상사가 직속 부하에게 전달할 수 있는 경우의 수 중 최소값이 된다.

# 🚨 참고로 트리 형식이다. 상사 or 부하가 겹치는 경우 X!


# 1. DFS 재귀로 풀이
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    
    for i, boss in enumerate(map(int, input().split())):
        if i == 0:
            continue
        graph[boss].append(i)
    
    """
    만약 부하가 3명이 있고 부하의 부하들에게 전하는데에 걸리는 시간이 다음과 같다고 치자.
    부하1: 5분 / 부하2: 1분 / 부하3: 0분(부하 X)
    3 -> 2 -> 1 순서로 전하게 되면 이렇게 된다.
    ex) x번: x번 본인이 전달받는데까지 걸리는 시간 + x번의 부하들에게 전달하는 시간
    - 3번: 1 + 0 = 1분
    - 2번: 2 + 1 = 3분
    - 1번: 3 + 5 = 8분
    => 최종적으로 걸리는 시간은 8분

    1 -> 2 -> 3 순서로 전하면?
    - 1번: 1 + 5 = 6분
    - 2번: 2 + 1 = 3분
    - 3번: 3 + 0 = 3분
    => 최종적으로 걸리는 시간은 6분

    따라서 딸린 자식이 가장 많은 부하에게 제일 먼저 전달해줘야한다.
    """

    def dfs(node):
        # 부하들의 일처리 시간
        times = []

        for child in graph[node]:
            times.append(dfs(child))
        
        times.sort(reverse=True)
        max_time = 0

        # i: 해당 부하에게 전달하는데까지의 시간
        # time: 해당 부하가 자신의 부하들에게 전달하는 시간
        for i, time in enumerate(times, start=1):
            max_time = max(max_time, i + time)
        return max_time
    
    print(dfs(0))


main()


# 2. 재귀 없이 스택만 사용하기
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    graph = [[] for _ in range(N)]

    for i, boss in enumerate(map(int, input().split())):
        if i == 0:
            continue
        graph[boss].append(i)
    
    # 🗝️ stack1 과정을 통해 stack2에 부모-자식 순서로 저장되게끔 처리한다.
    stack1 = [0]
    stack2 = []

    while stack1:
        curr = stack1.pop()

        stack2.append(curr)
        for nxt in graph[curr]:
            stack1.append(nxt)
    
    # dp[x]: x번 직원이 뉴스를 들은 후, 자신의 모든 직속 부하들에게 뉴스를 전파하는데 걸리는 최소 시간
    dp = [0] * N

    while stack2:
        curr = stack2.pop()

        times = []
        for child in graph[curr]:
            times.append(dp[child])
        
        # 오래 걸리는 자식부터 처리
        times.sort(reverse=True)

        max_time = 0
        for i, time in enumerate(times, start=1):
            max_time = max(i + time, max_time)
        
        dp[curr] = max_time
    
    print(dp[0])


main()