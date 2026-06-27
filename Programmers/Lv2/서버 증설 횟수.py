# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/389479

# 현재 서버 상태를 * 24 배열로 관리하는 방법도 있음. <- 더 편리함. 괜히 pop(0)를 쓰는것보다 나음.
from sys import stdin


input = stdin.readline

def solution(players: list, m: int, k: int) -> int:
    cnt = 0
    state = []
    
    for i, player in enumerate(players):
        s = 0
        while s < len(state) and state[s] <= i:
            state.pop(0)
            
        n = player // m
        
        if len(state) < n:
            for _ in range(n - len(state)):
                cnt += 1
                state.append(i + k)
        
    return cnt