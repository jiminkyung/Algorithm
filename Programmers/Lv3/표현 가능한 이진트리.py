# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/150367


import sys


sys.setrecursionlimit(10**6)

def solution(numbers: list[int]) -> list[int]:
    def check(num: str) -> bool:
        """
        num: 현재 서브트리

        어떤 노드(root)가 더미 노드일때, 그 노드의 서브트리에 실제 노드가 존재하면 False.
        루트, 서브트리 모두 더미 노드로 구성되어 있다면 True를 반환.
        """
        L = len(num)

        if L == 1:
            return True
        
        mid = L // 2
        root = num[mid]

        if root == "0":
            return all(n == "0" for n in num)
        
        # root를 기준으로 왼쪽, 오른쪽 서브트리로 나누어 검사
        left = check(num[:mid])
        right = check(num[mid + 1:])

        # 왼쪽, 오른쪽 모두 조건을 만족한다면 True
        if left and right:
            return True
        
        return False
    

    ret = []

    for number in numbers:
        binary = bin(number)[2:]

        # 길이가 2^k - 1이 되도록 앞에 0 채워넣기
        L = 1
        while L < len(binary):
            L = L*2 + 1  # 1, 3, 7... -> 이전 값*2 + 1
        
        binary = binary.zfill(L)

        if check(binary):
            ret.append(1)
        else:
            ret.append(0)
    
    return ret