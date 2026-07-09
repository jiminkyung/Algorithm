# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/148653

# 뒷자리부터 하나씩 체크.
# 0~4 일경우 내리고, 6~ 일 경우 올림.
# 만약 딱 5라면, 다음자리(앞자리) 숫자를 확인해본다.
# 앞자리 수가 5~ 라면 올린 후 캐리 1 증가, 0~4 라면 내린다.
def solution(storey):
    stone = 0
    
    while storey:
        curr = storey % 10
        
        if 0 <= curr < 5:
            stone += curr
        else:
            if curr == 5:
                nxt = (storey // 10) % 10
                if 0 <= nxt < 5:
                    stone += 10 - curr
                else:
                    storey += 10
                    stone += curr
            else:
                stone += 10 - curr
                storey += 10
        
        storey //= 10
            
    return stone


# 정리한 버전
def solution(storey):
    stone = 0
    
    while storey:
        storey, curr = storey // 10, storey % 10
        
        if curr == 5:
            nxt = storey % 10
            if nxt >= 5:
                storey += 1
                curr = 10 - curr
        else:
            if curr >= 5:
                curr = 10 - curr
                storey += 1
        stone += curr
        
    return stone