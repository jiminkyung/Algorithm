# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43165

# BFS / DFS 모두 가능함.
from sys import stdin


input = stdin.readline

def solution(numbers: list[int], target: int):
    answer = 0
    N = len(numbers)
    
    def dfs(idx: int, curr: int):
        # idx: 현재 계산할 인덱스, curr: idx-1번째까지의 값을 계산한 결과
        nonlocal answer
        
        if idx == N:
            if curr == target:
                answer += 1
            return
        
        dfs(idx + 1, curr + numbers[idx])
        dfs(idx + 1, curr - numbers[idx])
        return
    
    dfs(0, 0)
    return answer