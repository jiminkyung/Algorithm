# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    t, hp, hhp = bandage
    curr = health

    prev = None
    for i, (time, damage) in enumerate(attacks):
        if prev:
            term = time - attacks[i-1][0] - 1
            cnt = term // t
            # 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 붕대 감기를 다시 사용.
            # 🚨 term 내에 붕대감기를 여러번 성공할 수 있음.
            curr += term * hp + cnt * hhp
            
            curr = min(health, curr)  # 최대 체력을 넘어서지 않게
        
        prev = time
        curr -= damage

        if curr <= 0:
            return -1
    
    return curr