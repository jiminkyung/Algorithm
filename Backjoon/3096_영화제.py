# 수학
# 브루트포스 알고리즘
# 조합론


# 문제: https://www.acmicpc.net/problem/3096
# 메모리: 35480KB / 시간: 2816ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    # grpah[i]: 왼쪽마을 i와 이어져있는 오른쪽마을
    graph = [[] for _ in range(N)]
    left = set()

    for _ in range(M):
        l, r = map(int, input().split())
        graph[l-1].append(r-1)
        left.add(l-1)
    
    cnt = 0
    left = list(left)
    # 왼쪽마을 두개를 고르고, 이 두 마을이 갈 수 있는 오른쪽마을 갯수를 체크.
    for i in range(len(left)):
        l1 = set(graph[left[i]])

        if len(l1) < 2:  # 이미 두개가 안된다면 패스
            continue

        for j in range(i+1, len(left)):
            l2 = set(graph[left[j]])
            l = l1 & l2

            # l개의 오른쪽 마을에서 2개를 선택할 경우의 수
            if len(l) >= 2:
                cnt += len(l) * (len(l)-1) // 2
    
    print(cnt)


main()