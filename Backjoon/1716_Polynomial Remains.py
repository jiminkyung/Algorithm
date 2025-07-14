# 수학


# 문제: https://www.acmicpc.net/problem/1716

# 수학 문제... 나중에 다시 풀어볼만 함.
# 메모리: 33432KB / 시간: 52ms
from sys import stdin


input = stdin.readline

def main():
    """
    나머지 정리를 이용한 다항식 나머지 계산이 필요함.
    원래의 식이 아래와 같을때,
    f(x) = 몫 × (x^k + 1) + 나머지

    x^k + 1 = 0이 되는 조건(x^k = -1)을 이용하면,
    f(x) = 몫 × ((-1) + 1) + 나머지
         = 몫 × 0 + 나머지  
         = 나머지

    즉, 원래 다항식에서 x^k를 -1로 치환한 결과가 나머지인 셈.
    """
    while True:
        N, K = map(int, input().split())

        if (N, K) == (-1, -1):
            break

        lst = list(map(int, input().split()))
        max_c = 0  # 나머지 중 가장 큰 차수
        rest = [0] * K  # 나머지 값들 (K 차수 미만)

        if K == 0:
            print(0)
            continue

        for i in range(N+1):
            # 차수가 K 미만이라면 그대로 저장
            if i < K:
                rest[i] = lst[i]
                max_c = max(max_c, i)
            # K 이상이라면, x^k를 -1로 변환 후 계산
            else:
                t = i // K  # 변환 후 -1의 갯수
                r = i % K   # 변환 후 나머지의 차수
                # x^k가 짝수번 나타나면 +, 홀수번이라면 -
                if t % 2 == 0:
                    rest[r] += lst[i]
                else:
                    rest[r] -= lst[i]
                max_c = max(max_c, r)


        print(*rest[:max_c+1])


main()