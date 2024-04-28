"""
progresses와 speeds를 직접 조작하지 않는 코드.
"""

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    
    while progresses:
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
            
    answer.append(count)
    
    return answer