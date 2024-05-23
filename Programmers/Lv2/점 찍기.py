"""
실행시간에서 fail, 두번째 코드는 AI를 통해 수학적 요소를 추가했다.
"""

# 첫번째 코드. 맞지만 시간 초과.
def solution(k, d):
    ret = []

    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            if (i*i + j*j) > d*d:
                break
            if j >= 10:
                ret.append((j//10, j%10))
            else:
                ret.append((i, j))

    return len(ret)

# 두번째 시도. 실행시간이 훨씬 단축되었다.
def solution(k, d):
    """
    한번의 for문을 통해 x, y 둘 다 체크 가능.
    x를 베이스로 잡고, 이 기준으로 계산했을때 가능한 y의 최대 거리를 max_y로 선언한다.
    max_y를 k로 나눠 k의 배수가 몇 개 나오는지 계산한 뒤 1을 더해준다. 0도 포함되기 때문.
    """
    ret = 0

    for x in range(0, d+1, k):
        max_y = int((d*d - x*x) ** 0.5)
        ret += (max_y // k) + 1

    return ret