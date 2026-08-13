# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/389478


def solution(n, w, num):
    # num이 위치한 행/열 계산
    row = (num - 1) // w
    col = num % w

    # 만약 행의 끝에 위치한 값이라면, w로 저장. (숫자가 0이 아닌 1부터 시작하기 때문)
    if col == 0:
        col = w
    
    # num 위의 숫자들은 두 개의 텀으로 존재함.
    # val = [홀수번째 간격, 짝수번째 간격]
    # num 위의 숫자들을 x1, x2, x3... 라고 할 때, 각 값은 num + val[0], x1 + val[1], x2 + val[0] 이 되는 셈.
    val = [(w - col) * 2 + 1, max(0, (col - 1)) * 2 + 1]

    # 전체 행의 갯수
    r = (n - 1) // w

    # 일단 num ~ 맨 끝까지의 행 갯수만큼 cnt 저장.
    cnt = r - row + 1
    last = num + sum(val) * ((r - row) // 2)  # num 위에 존재할 수 있는 숫자들 중 마지막 값.
    
    # 만약 num 위의 행 수가 홀수개라면, val[0]값을 추가로 더해줌.
    if row % 2 != r % 2:
        last += val[0]
    
    # 최종적인 last 값이 n보다 크다면, 마지막 행은 없는셈이므로 cnt 감소.
    if last > n:
        cnt -= 1
    
    return cnt