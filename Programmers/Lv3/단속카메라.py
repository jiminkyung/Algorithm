# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes: list[list[int]]) -> int:
    # 🗝️ 진출값을 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])

    out = -30001  # 가장 최근에 설치한 카메라의 위치
    cnt = 0

    for i, o in routes:
        # 만약 in/out 지점을 카메라로 잡을 수 있다면 pass
        if i <= out <= o:
            continue

        # 아니라면 카메라를 추가로 설치하고, 최근 카메라 위치값을 현재 차량의 진출값으로 갱신.
        cnt += 1
        out = o
    
    return cnt