# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/181188


# DP를 써야하나 싶었지만? 그리디로 푸는 문제.
def solution(targets: list[list[int]]) -> int:
    targets.sort(key=lambda x: x[1])

    # 키포인트는 끝나는 지점. (y 좌표) 기준으로 오름차순 정렬.
    # 만약 (1, 7), (2, 5), (3, 4) 가 있다면, 4를 기준으로 한번 쏜다. end point는 4로 저장.
    # 그리고 좌표를 하나씩 체크. -> 시작 지점이 이전 end point(4)와 같거나 클 경우 추가 요격.
    end = -1
    cnt = 0

    for s, e in targets:
        if end <= s:
            cnt += 1
            end = e
    
    return cnt