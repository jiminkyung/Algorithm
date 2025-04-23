# 수학


# 문제: https://www.acmicpc.net/problem/1188

# 이해하기 힘들었던 문제다... 질문게시판에 설명글이 있어서 참고했다.
# 👉 https://www.acmicpc.net/board/view/148587

# 사실상 풀었다고 할 수 없는 문제다. 로직 이해가 중요 포인트다.
# 내가 명확히 설명할 수 있을만큼 이해해야함... 다시 봐야 할 문제.

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    """
    N * x = M * y 
    (x: 소시지를 나눈 전체 조각 수, y: 한 사람에게 주는 조각 수)
    소시지 N개를 공평하게 나누기 위해, 조각 수 x와 사람 수 M 사이의 비례식을 세움.

    이 식을 단순화하기 위해 N과 M의 최대공약수 c를 이용함.
    => N = a * c, M = b * c 라고 두면 (a = N // c, b = M // c)

    식을 다시 쓰면 (a * c) * x = (b * c) * y,
    c를 약분하면 a * x = b * y 가 됨.

    이 식을 만족하는 가장 작은 자연수 해는 x = b, y = a
    => 소시지 하나를 b조각 내고, 사람 하나당 a조각씩 주면 정확히 나눠 떨어진다는 뜻.

    이런 패턴(블럭)이 최대공약수 c개 존재함 -> 같은 방식으로 c번 반복하면 전체 소시지를 나눌 수 있음.

    블럭 하나당 필요한 칼질 수는 (b - 1)
    총 블럭이 c개니까 전체 칼질 수는 c * (b - 1)
    => 정리하면 M - gcd(N, M)
    """

    print(M - gcd(N, M))


main()