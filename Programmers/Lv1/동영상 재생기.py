# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/340213

def solution(video_len, pos, op_start, op_end, commands) -> str:

    def calc(time: str) -> int:
        hh, mm = map(int, time.split(":"))
        return hh * 60 + mm
    

    # 모두 분 단위로 환산
    video_len = calc(video_len)
    pos = calc(pos)
    op_start = calc(op_start)
    op_end = calc(op_end)

    # 시작 전, 만약 현재 위치가 오프닝 구간이라면 건너뜀.
    if op_start <= pos < op_end:
        pos = op_end
    
    for cmd in commands:
        if cmd == "prev":
            pos = max(pos - 10, 0)
        else:
            pos = min(pos + 10, video_len)
        
        if op_start <= pos < op_end:
            pos = op_end
    
    return f"{pos // 60:02d}:{pos % 60:02d}"