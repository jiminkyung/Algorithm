# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules: list[int], timelogs: list[list[int]], startday: int):
    L = len(schedules)
    cnt = L

    # 각 사원별로 체크
    for i in range(L):
        d = startday
        s_hh, s_mm = schedules[i] // 100, schedules[i] % 100
        s_mm += 10
        
        # 60분 이상이라면 hh += 1 처리
        if s_mm >= 60:
            s_hh = (s_hh + 1) % 24
            s_mm %= 60
        
        s = s_hh * 100 + s_mm
        
        # 일주일치를 요일별로 확인
        for j in range(7): 
            if (d + j) % 7 in (6, 0):
                continue
            
            t_hh, t_mm = timelogs[i][j] // 100, timelogs[i][j] % 100
            
            t = t_hh * 100 + t_mm
            
            # 희망 시각을 초과하는 날이 하루라도 존재한다면 카운트 -1 후 다음 직원으로 넘어감.
            if t > s:
                cnt -= 1
                break
    return cnt