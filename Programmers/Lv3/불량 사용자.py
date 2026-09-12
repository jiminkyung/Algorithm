# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/64064


def solution(user_id: list[str], banned_id: list[str]) -> int:
    N, M = len(user_id), len(banned_id)

    def check(ban_id: str, user_id: str) -> bool:
        """
        불량 사용자 아이디 ban_id와 user_id를 매칭할 수 있는지 확인하는 함수.
        """

        # 길이가 다르다면 바로 False 반환
        if len(ban_id) != len(user_id):
            return False
        
        # 해당 위치 문자열 조건이 일치하지 않을 경우 False 반환
        for i in range(len(ban_id)):
            if ban_id[i] != "*" and ban_id[i] != user_id[i]:
                return False
        
        return True
    

    ret = set()


    def dfs(curr: int, idx: int):
        """
        curr: 선택 가능한 아이디 인덱스를 비트마스킹으로 표현한 값. 1 가능 0 불가능
        idx: 현재 적용할 불량 사용자 아이디 인덱스

        curr을 탐색하며 banned_id[idx]를 적용할 아이디를 고른다.
        해당 아이디에 banned_id[idx]를 적용할 수 있다면 다음 DFS 실행. dfs(갱신한 curr, idx + 1)
        """
        nonlocal ret

        # 모든 불량 아이디를 확인했다면 결과 set에 저장
        if idx == M:
            ret.add(curr)
            return
        
        for i in range(N):
            if curr & (1 << i) and check(banned_id[idx], user_id[i]):
                dfs(curr & ~(1 << i), idx + 1)
    

    dfs((1 << N) - 1, 0)
    return len(ret)