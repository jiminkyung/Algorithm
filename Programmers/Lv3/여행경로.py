# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets: list[list[str]]) -> list[str]:
    # ticket[출발지] = [(도착지, tickets에서의 인덱스)...]
    ticket = {}

    for i, (f, t) in enumerate(tickets):
        ticket.setdefault(f, []).append((t, i))
    
    # 각 출발지의 도착지 후보들을 오름차순으로 정렬해줌.
    # -> 가능한 경로가 여러개일 경우 알파벳 순서가 앞서는 경로를 택해야 하기 때문.
    for f in ticket:
        ticket[f].sort()
    
    visited = [False] * len(tickets)
    ret = []


    def dfs(prev: str, log: list[str]):
        nonlocal ret

        # 모든 항공권을 사용했을 경우 log 저장
        # 위에서 이미 오름차순으로 정렬해놨으니, 첫 번째로 나온 ret이 곧 정답인 셈.
        if len(log) == len(tickets) + 1:
            ret = log[:]
            return
        
        # 만약 위 조건에 반하고 도착지로만 존재하는 공항이라면, 더이상 진행할 수 없으므로 바로 return
        if prev not in ticket:
            return
        
        # 현재 공항을 출발지로 하여 갈 수 있는 도착지들을 하나씩 방문
        for t, idx in ticket[prev]:
            if not visited[idx]:
                visited[idx] = True
                dfs(t, log + [t])
                visited[idx] = False
            
            # ret이 나온 상태라면 더이상 확인할 필요 X
            if ret:
                return
    

    dfs("ICN", ["ICN"])
    return ret


# 도움이 됐던 예제
print(solution([["ICN", "JFK"], ["ICN", "JFK"], ["JFK", "HND"], ["HND", "ICN"], ["JFK", "ATL"]]))