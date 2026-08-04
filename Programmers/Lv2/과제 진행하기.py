# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/176962

# 조건 문제
def solution(plans: list[list[str]]) -> list[str]:
    ret = []
    stopped = []

    # 시작시간이 빠른 순서대로 정렬.
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        sub, start, time = plans[i]
        hh, mm = map(int, start.split(":"))
        start = hh * 60 + mm  # 분 단위로 환산

        end = start + int(time)

        # 다음에 새로 시작해야 할 과목이 남아있는경우
        if i < len(plans)-1:
            hh, mm = map(int, plans[i+1][1].split(":"))
            start = hh * 60 + mm

            gap = start - end
            
            # 1. 여유시간이 없다면 현재 과목 중단.
            if gap < 0:
                stopped.append((sub, -gap))
            # 2. 정확히 떨어지는 경우 끝낸 과목으로 처리.
            elif gap == 0:
                ret.append(sub)
            # 3. 여유시간이 있다면, 끝낸 과목으로 처리 후 중단했던 과목 실행.
            else:
                ret.append(sub)
                while stopped and gap > 0:
                    stopped_sub, remain_time = stopped.pop()
                    gap -= remain_time

                    if gap < 0:
                        stopped.append((stopped_sub, -gap))  # 덜 끝냈다면 수행한 시간만큼 감소 후 리스트에 도로 추가.
                        break
                    else:
                        ret.append(stopped_sub)
        # 현재 과목이 마지막 시작 과목일경우 바로 끝낸 과목으로 처리.
        else:
            ret.append(sub)
    
    # 🚨 남아있는 중단된 과목은 최근에 중단한 순서대로(거꾸로) 실행.
    for sub, _ in stopped[::-1]:
        ret.append(sub)
    
    return ret