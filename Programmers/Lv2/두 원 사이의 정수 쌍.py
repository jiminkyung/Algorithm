# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/181187


# 단순 수학문제
def solution(r1, r2):
    # r2 > r1

    # 작은 원 r1 경계 내에 존재하는 점의 갯수
    cnt_1 = 0
    x = r1

    # 1사분면(x축 위의 점 포함, y축 위의 점 포함 X)의 점 갯수를 구함.
    for y in range(r1):
        while x**2 + y**2 >= r1**2:
            x -= 1
        cnt_1 += x
    
    # 4사분면이니 4배로 곱해준 후 +1(원점) 추가.
    # 애초에 1사분면을 구할 때 x, y 중 한 축만 포함하도록 계산했으므로 중복은 따로 처리할 필요 없음.
    cnt_1 = cnt_1 * 4 + 1

    # 큰 원 r2는 경계를 포함해서 계산
    cnt_2 = 0
    x = r2

    for y in range(r2):
        while x**2 + y**2 > r2**2:
            x -= 1
        cnt_2 += x
    
    cnt_2 = cnt_2 * 4 + 1

    return cnt_2 - cnt_1