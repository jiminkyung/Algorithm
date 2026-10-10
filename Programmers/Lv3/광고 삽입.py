# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72414


# 구현 연습하기 좋은 문제
def solution(play_time: str, adv_time: str, logs: list[str]) -> str:
    def convert(time: str) -> int:
        """ hh:mm:ss 형태의 시간 데이터를 초 단위 정수형 데이터로 변환하는 함수 """
        hh, mm, ss = map(int, time.split(":"))
        return hh * 3600 + mm * 60 + ss
    

    # times[x]: x초에 시청중인 사람의 
    # 시청시간 중 (가장 빠른 시작 시간 ~ 가장 늦는 종료 시간) 길이만큼 times를 생성하려 했으나?
    # 예제3 같은 케이스일경우 막혀버림.
    # 🚨 즉, 광고 시간이 시청시간 범위보다 클 경우, 제대로 된 답이 나오지 않음. (0 ~ 재생시간) 만큼 생성해야 함.
    # -> 기존 방식대로 하면 광고 시작 시간은 시청시간 범위 내에서만 존재해버리기 때문.
    play_time = convert(play_time)
    adv_time = convert(adv_time)

    time_logs = []  # 시청시간을 초 단위로 변환하여 (시작시간, 종료시간) 형태로 저장

    for log in logs:
        start, end = log.split("-")

        start = convert(start)
        end = convert(end)
        
        time_logs.append((start, end))
    
    times = [0] * (play_time + 1)

    # 차분 배열 방식을 사용하여 times 갱신
    # 구간을 [start, end) 로 취급하여 계산. (2초에서 6초까지 재생했다면 4초동안 재생한것이므로)
    for start, end in time_logs:
        times[start] += 1
        times[end] -= 1
    
    for i in range(1, play_time):
        times[i] += times[i-1]
    
    # 슬라이딩 윈도우 방식으로 계산 (또는 누적합을 사용해서 계산하는 방식도 가능)
    max_time = time = sum(times[:adv_time])
    start = 0
    
    for i in range(1, play_time - adv_time + 1):
        time -= times[i-1]  # 이전 시작시간 빼기
        time += times[i + adv_time - 1]  # 새로운 끝나는시간 더해주기

        if time > max_time:
            max_time = time
            start = i
    
    # 초 단위 시간을 hh:mm:ss 형태로 재변환
    hh = mm = ss = 0

    hh = start // 3600
    start %= 3600
    mm = start // 60
    start %= 60
    ss = start

    ret = f"{hh:02d}:{mm:02d}:{ss:02d}"
    return ret