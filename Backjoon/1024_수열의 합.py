# 수학


# 문제: https://www.acmicpc.net/problem/1024
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, L = map(int, input().split())
    """
    x부터 시작해서 길이가 k인 연속된 수들의 합은?
    수식은 x + (x+1) + (x+2) + ... (x+(k-1)) 일것임.

    정리하면,
    x가 k번 더해짐 => kx
    나머지 부분은 0 + 1 + ... + (k-1) 이니까 등차수열 공식을 사용하면 됨.
    => (k-1)*k / 2
    전체 합은 kx + (k-1)*k / 2 가 되겠다.

    이게 N이 돼야하는 상황이니까,
    kx + (k-1)*k / 2 = N 여기에 2를 곱해서 분모를 통일해주고
    => 2kx + (k-1)*k = 2N
    이걸 x에 대해서 풀면...
    x = (2N - (k-1)*k) / 2k 가 되겠다.
    """

    ret = [-1]

    for k in range(L, 101):
        top = 2 * N - (k-1) * k
        bottom = 2 * k

        if top % bottom == 0:  # "정수"리스트이므로 정확히 나누어떨어져야 함.
            x = top // bottom
            if x >= 0:  # x가 0 이상일경우에만 ret 갱신
                ret = [x+i for i in range(k)]
                break
    
    print(*ret)


main()