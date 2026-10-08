# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42892


# 트리, 그래프 문제
import sys


sys.setrecursionlimit(10**6)

def solution(nodeinfo: list[list[int, int]]) -> list[list, list]:
    # tree[i] = i번 노드의 [왼쪽 자식노드, 오른쪽 자식노드, 부모노드] 형태로 구성
    N = len(nodeinfo)
    tree = [[None, None, None] for _ in range(N)]

    nodes = [(x, y, i) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))  # y값이 클수록 상위 레벨, x값이 작을수록 왼쪽에 위치

    def dfs(sub_nodes: list[list[int]], parent: int):
        nonlocal tree

        # 서브트리가 없다면(리프 노드라면) return
        if not sub_nodes:
            return
        
        # y값 기준으로 정렬했으므로, 첫번째에 저장되어있는 노드 == 현재 서브트리의 루트 노드인 셈.
        root = sub_nodes[0]
        x, y, idx = root

        # 부모 노드의 번호 저장
        tree[idx][2] = parent

        left = []
        right = []

        # 현재 루트를 기준으로 x값이 작으면 왼쪽, 크면 오른쪽 서브트리
        for node in sub_nodes[1:]:
            if node[0] < x:
                left.append(node)
            else:
                right.append(node)
        
        # 새로 분류한 왼쪽/오른쪽 서브트리의 루트 노드(직계 자식 노드) 저장
        left_child = dfs(left, idx)
        right_child = dfs(right, idx)

        tree[idx][0] = left_child
        tree[idx][1] = right_child

        return idx
    

    root_idx = dfs(nodes, None)

    pre_path = []
    post_path = []


    def preorder(curr):
        """ 전위 순회 함수. root - left - right 순서 """
        nonlocal pre_path

        # 노드가 존재하지 않다면 return
        if curr is None:
            return
        
        # 현재 노드(root)를 path에 저장 후, 왼쪽 - 오른쪽 순서로 전위 순회 dfs
        pre_path.append(curr + 1)
        l, r, _ = tree[curr]    
        preorder(l)
        preorder(r)
    

    def postorder(curr):
        """ 후위 순회 함수. left - right - root 순서 """
        nonlocal post_path

        if curr is None:
            return
        
        # 왼쪽 - 오른쪽 순서로 전위 순회 dfs 진행 후 현재 노드(root)를 path에 저장
        l, r, _ = tree[curr]
        postorder(l)
        postorder(r)
        post_path.append(curr + 1)
    

    preorder(root_idx)
    postorder(root_idx)

    return [pre_path, post_path]