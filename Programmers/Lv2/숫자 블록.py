# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12923


def solution(begin, end):
    ret = []

    for num in range(begin, end+1):
        if num == 1:
            ret.append(0)
            continue

        max_num = 1

        # num의 제곱근까지 탐색.
        # num번째 위치에 들어갈 값 = num의 약수 중 num보다 작고 10,000,000 이하인 값.
        for i in range(2, int(num ** 0.5) + 1):
            # 나누어 떨어질경우, 몫이 10,000,000 이하인지 확인함.
            if num % i == 0:
                if num // i <= 10000000:
                    max_num = num // i  # 조건을 만족한다면 몫(num // i) 저장.
                    break
                else:
                    # 10,000,000보다 클 경우, i를 저장.
                    # max_num = max(i, max_num)
                    max_num = i
        
        ret.append(max_num)
    
    return ret