# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43163


def solution(begin: str, target: str, words: list[str]) -> int:
    # 타겟이 words 안에 없거나, 이미 타겟인 상태라면 바로 0 반환.
    if target not in set(words) or begin == target:
        return 0
    
    
    def dfs(curr: str, cands: set[str]) -> int:
        """
        DFS 방식으로 현재 단어에서 한 글자씩 바꿔가며 최솟값 갱신.
        curr: 현재 단어
        cands: 변환 가능한 단어 후보들 (아직 사용 X)
        """
        if curr == target:
            return len(words) - len(cands)
        
        min_cnt = int(1e9)
        
        for cand in cands:
            # 🚨 위치도 중요. 전체 글자에서 정확히 한 번만 바꿀수 있음.
            if sum(cand[i] != curr[i] for i in range(len(cand))) == 1:
                min_cnt = min(min_cnt, dfs(cand, cands - {cand}))  # 선택한 단어를 제외한 단어 후보들을 넘겨줌
        
        return min_cnt
    
    
    ret = dfs(begin, set(words))
    return ret