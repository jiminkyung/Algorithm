# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/152996

def solution(weights):
    ret = 0
    weights.sort()
    cnt = {}  # cnt[weight]: 무게가 weight인 사람의 갯수
    for weight in weights:
        cnt[weight] = cnt.get(weight, 0) + 1
    
    lst = [2, 3, 4]
    
    for w, val in cnt.items():
        # 2명 이상이면 nC2 조합 구함, 1명일 경우 그냥 1
        comb = max(val * (val-1) // 2, 1)
        if val >= 2:  # 2명 이상이면 위에서 구한 조합의 수를 결과값에 더해줌.
            ret += comb
        
        for i in range(3):
            for j in range(i+1, 3):
                # (2, 3), (2, 4), (3, 4) 형태로 검사해야 중복없이 검사 가능.
                if w * lst[i] % lst[j] == 0:  # 무게 * n 한 값을 n+a로 나눴을때의 값이 정수일때만 검사.
                    new_val = cnt.get((w * lst[i]) // lst[j], 0)
                    ret += val * new_val  # 정수이고, 존재하는 무게라면 현재 무게의 인원 수 * 해당 무게의 인원 수 계산 후 결과값에 더해줌.
            
    return ret