# 트리


# 이진 트리를 입력받아 순회하는 문제.
# 참고👉 https://velog.io/@ohk9134/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-python-%ED%8A%B8%EB%A6%AC-%EA%B5%AC%ED%98%84
# 클래스 + 재귀로 구현하는 방식👉 https://define-me.tistory.com/79

# 메모리: 31120KB / 시간: 32ms

from sys import stdin


input = stdin.readline

# 전위순회: ROOT - L - R
def preorder(tree, root):
    if root != ".":
        print(root, end="")            # ROOT
        preorder(tree, tree[root][0])  # L
        preorder(tree, tree[root][1])  # R

# 중위순회: L - ROOT - R
def inorder(tree, root):
    if root != ".":
        inorder(tree, tree[root][0])  # L
        print(root, end="")           # ROOT
        inorder(tree, tree[root][1])  # R

# 후위순회: L - R - ROOT
def postorder(tree, root):
    if root != ".":
        postorder(tree, tree[root][0])  # L
        postorder(tree, tree[root][1])  # R
        print(root, end="")             # ROOT


N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")