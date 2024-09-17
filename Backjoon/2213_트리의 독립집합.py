# 트리에서의 동적 계획법


# 문제: https://www.acmicpc.net/problem/2213
# 메모리: 34188KB / 시간: 60ms
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    """
    해당 노드에 연결된 간선을 탐색하며 dp를 업데이트하는 함수
    - dp[노드][1] = 해당 노드를 선택할 경우
    - dp[노드][0] = 해당 노드를 선택하지 않을 경우
    """
    dp[node][1] = value[node]
    
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            # 해당 노드를 선택하지 않을 경우, 자식 노드는 선택해도 되고 안해도 된다.
            dp[node][0] += max(dp[child][1], dp[child][0])
            # 해당 노드를 선택한다면 자식 노드는 선택할 수 없다.
            dp[node][1] += dp[child][0]

def trace(node, parent, selected: bool):
    """
    dp를 추적하며 선택된 노드들을 저장하는 함수
    - selected: bool값. dp[노드][1] > dp[노드][0]의 결과가 참이라면 True, 아니면 False.
    """
    if selected:
        ret.append(node)
        for child in tree[node]:
            if child != parent:
                # 현재 노드를 선택했다면 자식 노드는 선택하지 않은것으로(selected == False) 실행.
                trace(child, node, False)
    else:
        for child in tree[node]:
            if child != parent:
                # 해당 노드를 선택하지 않았다면, 자식노드를 선택한 값, 선택하지 않은 값을 비교
                if dp[child][1] > dp[child][0]:
                    # 자식노드를 선택한 값이 더 크다면 True로 실행
                    trace(child, node, True)
                else:
                    # 아니라면 False로 준다.
                    trace(child, node, False)


n = int(input())
value = [0] + list(map(int, input().split()))

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]

dfs(1, 0)

max_sum = max(dp[1][0], dp[1][1])

ret = []
trace(1, 0, dp[1][0] < dp[1][1])
ret.sort()

print(max_sum)
print(*ret)