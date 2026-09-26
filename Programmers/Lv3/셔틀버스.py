# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17678


# 구현 문제
def solution(n, t, m, timetable: list[str]) -> str:
    table = []

    # 분단위로 변환 후 오름차순으로 정렬
    for time in timetable:
        hh, mm = map(int, time.split(":"))
        time = hh * 60 + mm
        table.append(time)
    
    table.sort()
    start = 540  # 셔틀 시작시간은 오전 9시로
    idx = 0

    # 마지막 셔틀버스 직전(n-1) 까지만 반복
    for _ in range(n-1):
        cnt = 0  # 현재 버스에 탑승한 인원 수
        while idx < len(table) and cnt < m:
            # idx번째 크루가 서는 시간이 현재 버스시간 이후라면 break
            if table[idx] > start:
                break

            cnt += 1
            idx += 1
        
        # 다음 버스 시간으로 갱신
        start += t
    
    # 마지막 버스(n)에 탈 수 있는 인원 체크
    cnt = 0

    while idx < len(table) and cnt < m:
        if table[idx] > start:
            break

        cnt += 1
        idx += 1

    # 만약 마지막 버스 탑승인원이 m명이라면, (탑승한 크루 중 마지막 크루의 시간) -1분 한 시간이 정답.
    if cnt == m:
        ret = table[idx - 1] - 1
    # 인원이 m명 미만일경우 가장 늦은 시간 = 버스 출발시간이므로, 마지막 버스의 출발시간이 정답.
    else:
        ret = start
    
    # hh:mm 단위로 다시 변환
    ret = f"{ret // 60:02d}:{ret % 60:02d}"
    return ret