# 트리


"""
# 참고👉 https://ku-hug.tistory.com/135
# 참고👉 https://velog.io/@cjkangme/%EB%B0%B1%EC%A4%80-2263.-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC

인오더(중위순회), 포스트오더(후위순회)가 주어졌을때, 프리오더(전위순회)값을 구해야한다.

앞전의 트리순회 문제에서 예시데이터를 가져와보자.
preorder: ABDCEFG
inorder: DBAECFG
postorder: DBEGFCA

포스트오더의 제일 끝은 루트와 같다. => A

인오더에서 A를 기준으로 왼쪽은 왼쪽서브트리, 오른쪽은 오른쪽서브트리다.
왼: 루트(A)의 인덱스 - 인오더 시작 인덱스, 오: 인오더 끝 인덱스 - 루트(A)의 인덱스
=> 왼쪽서브트리, 오른쪽서브트리의 갯수

포스트오더의 제일 끝(루트)가 인오더에서 어느 위치에 있는지 구해야 함.
position[인오더의 i번째 값] = i => 포스트오더의 i번째 값은 인오더의 i에 위치한다.
"""

# 메모리: 72908KB / 시간: 288ms

import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**9)  # 재귀 깊이를 늘려줘야 함

# preorder(position, 인오더 시작인덱스, 인오더 끝인덱스, 포스트오더 시작인덱스, 포스트오더 끝인덱스)
def preorder(position, inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):  # 범위가 노드 하나일수도 있으므로 >=를 사용하면 안된다.
        return
    
    root = postorder[postEnd]

    left = position[root] - inStart
    right = inEnd - position[root]
    
    # 프리오더는 ROOT - 왼 - 오 순서이므로 루트값 출력, 왼쪽 서브트리 범위 실행, 오른쪽 서브트리 범위 실행 순서로 진행한다.
    print(root, end=" ")
    preorder(position, inStart, inStart+left-1, postStart, postStart+left-1)
    preorder(position, inEnd-right+1, inEnd, postEnd-right, postEnd-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i

preorder(position, 0, n-1, 0, n-1)