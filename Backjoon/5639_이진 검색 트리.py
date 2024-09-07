# 트리


"""
# 전위: 50 30 24 5 28 45 98 52 60
# 후위: 5 28 24 45 30 60 52 98 50

이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.
- 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
- 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
- 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

따라서 맨 왼쪽값은 루트, 루트 다음으로 작은값이 왼쪽 서브트리, 루트 다음으로 큰 값이 오른쪽 서브트리가 되겠다.
즉 [root][왼쪽 서브트리][오른쪽 서브트리] 형식으로 구성되어있는 셈이다.
(서브트리 한쪽만 존재하는 경우도 있다.)
"""

# 메모리: 33708KB / 시간: 2044ms

import sys


sys.setrecursionlimit(10**9)

preorder = list(map(int, sys.stdin.read().splitlines()))

def postorder(lst, start, end):
    if start > end:
        return
    
    root = lst[start]
    idx = start + 1
    
    # 루트보다 큰 값이 나오는 위치를 찾음 (오른쪽 서브트리의 시작점)
    while idx <= end and lst[idx] < root:
        idx += 1

    postorder(lst, start + 1, idx - 1)
    postorder(lst, idx, end)
    print(root)

postorder(preorder, 0, len(preorder) - 1)


# 다른 풀이도 발견. 리스트를 슬라이싱해서 바로 던져준다. => 메모리가 어마어마하다...
# 출처: https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-5639-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8A%B8%EB%A6%AC-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break


def solution(A):
    # 받은 배열 길이가 0이면 return
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        tempL = A[1:]
    
    #왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)