# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/152995


# 도움이 됐던 반례
# [[7, 1], [6, 6], [5, 4], [5, 4], [6, 6]] => 정답: 3
def solution(scores: list[list[int, int]]) -> int:
    N = len(scores)
    w = sum(scores[0])  # 완호의 점수
    ret = -1
    # 순회 시 완호의 점수인지 따로 확인해야 하므로 (점수1, 점수2, 고유번호) 형태로 저장.
    scores = [(s1, s2, i) for i, (s1, s2) in enumerate(scores)]

    # 점수1을 기준으로 내림차순 정렬
    scores.sort(reverse=True)
    passed = []  # 인센티브 검사에 통과한 직원들의 점수

    # 인센티브를 받지 못하는 조건은 "두 점수 모두 타 직원보다 낮은 경우가 한번이라도 있을 경우"임.
    # 내림차순 정렬 된 상태이므로, idx번째 직원은 idx + x 번째 직원보다는 점수1이 무조건 높은 상태.
    # 따라서 idx - x 번째 직원의 점수2보다 idx번째 직원의 점수2가 낮다면, 인센티브 급여 조건에 탈락됨.

    # 🚨 동점인 경우를 주의해야함.
    # 만약 idx = 2 ~ 5 직원들의 점수1이 같다고 했을때, idx = 5의 점수2가 idx = 2의 점수2보다 작을 수 있음.
    # 이런 경우 앞선 직원보다 점수2가 작다고 해도 인센티브 급여 조건에 탈락되지 않음.

    # 점수1을 기준으로 그룹화시킨 후, 같은 그룹 내의 직원들은 서로 비교 X. 이전 그룹의 점수2로 비교 후 평가해야함.
    # 그룹 내 점수2 최고점이 다음 그룹을 검사할때의 비교값이 됨.
    # -> 점수1은 앞선 그룹보다 무조건 낮고, 점수2는 한번이라도 낮은 경우가 있다면 탈락시켜야 하므로 최대값을 저장.

    max_score = None  # 이전 그룹까지의 점수2 최대값
    idx = 0
    while idx < N:
        s1, s2, i = scores[idx]
        max_s2 = 0  # 현재 그룹의 점수2 최대값

        while idx < N and scores[idx][0] == s1:
            s1, s2, i = scores[idx]
            if max_score is None or s2 >= max_score:
                passed.append(s1 + s2)
                # 완호가 급여 조건에 통과했다면 ret 갱신
                if i == 0:
                    ret = 0

            max_s2 = max(max_s2, s2)
            idx += 1
        
        if max_score is None:
            max_score = max_s2

        max_score = max(max_score, max_s2)

    # 완호가 통과했을 경우에만 진행
    # 내림차순으로 정렬 후 순위 확인 (동석차의 수만큼 다음 석차는 건너 뜀)
    if ret == 0:
        passed.sort(reverse=True)
        ret = passed.index(w) + 1
    
    return ret