# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/67258


# 투 포인터 느낌으로 풀이.
def solution(gems: list[str]) -> list[int, int]:
    status = {}
    N, M = len(gems), len(set(gems))
    ret = None
    prev = idx = 0  # prev는 왼쪽 포인터, idx는 오른쪽 포인터
    min_diff = N + 1

    while idx < N:
        # 보석의 갯수를 딕셔너리 status로 관리.
        # status[보석]: prev부터 idx까지의 해당 보석 갯수
        status[gems[idx]] = status.get(gems[idx], 0) + 1

        # status의 길이가 M 이라면 모든 보석을 포함한다는 의미이므로,
        # M 이 유지될때까지 prev를 오른쪽으로 한칸씩 이동시켜본다 -> 조건을 만족하는 가장 짧은 구간을 찾기 위해
        while prev < N and len(status) == M:
            if (idx - prev + 1) < min_diff:  # 이전 최소길이보다 짧다면 갱신
                min_diff = (idx - prev + 1)
                ret = [prev + 1, idx + 1]
            
            # prev를 이동시켰으니 해당 보석을 1 감소시키고, 0개가 될 경우엔 딕셔너리에서 아예 삭제
            status[gems[prev]] -= 1
            if status[gems[prev]] == 0:
                del status[gems[prev]]

            prev += 1
        
        # 오른쪽 포인터는 조건과는 상관없이 계속 이동
        idx += 1
        
    return ret