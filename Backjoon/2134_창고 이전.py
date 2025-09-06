# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2134

"""
맞았지만~~? 다른 코드를 보니 시간 차이가 난다 ㅜㅜ
-> 아래는 다른 코드들을 보고 다시 수정한 코드다. 나는 제일 낮은층 + 높은층 조합을 생각했지만... 필요없었다.
-> A > B든 B < A든 상관없이 A의 1층부터 비우고, B의 1층부터 채우면 됨. 덧셈의 조합이므로 결과는 같을수밖에 없음.

40ms 코드👉 https://www.acmicpc.net/source/85548845
-> limit을 구한다음 A에서 1층부터 limit개 까지만 검사. (시작비용)
-> 마찬가지로 B에서 1층부터 limit개 까지만 검사. (도착비용)
-> 어차피 덧셈이기때문에 총 합은 같다.

⭐굳이 매칭을 고려하지 않아도 되는 이유

"몇 층 물건을 몇 층에 보낼지"는 굳이 정하지 않아도 됨!

비용
= (출발층 + 도착층) × 물품수
= 출발층×물품수 + 도착층×물품수
-> 출발 비용과 도착 비용을 독립적으로 계산 가능

출발: 낮은 층부터 가져오기 (최소 비용)
도착: 낮은 층부터 채우기 (최소 비용)

따라서 어떻게 매칭해도 총합은 동일하다.
ex) 1층→3층, 3층→1층 = 1층→1층, 3층→3층
"""

# 1) A, B 모두 낮은층부터 검사
# 메모리: 33432KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    n, m, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    B = [int(input()) for _ in range(m)]

    # A와 B 중 합이 더 작은것이 x
    x = min(sum(A), sum(B))
    limit = x
    y = 0

    a = b = 0

    while limit and a < n and b < m:
        # A의 a층에 있는 물품 갯수가 B의 b층에 있는 물품 갯수보다 많다면
        if A[a] > B[b]:
            # B의 갯수만큼만 옮기고 전체에서 카운트
            y += (a+b+2) * B[b]
            limit -= B[b]
            # 옮긴 갯수만큼 A의 a층 값 수정
            A[a] -= B[b]
            b += 1
        else:
            y += (a+b+2) * A[a]
            limit -= A[a]
            B[b] -= A[a]
            a += 1

    print(x, y)


main()


# 2) 처음 풀이 (상황에 따라 다른 조합으로 검사)
# 메모리: 33432KB / 시간: 1784ms
from sys import stdin


input = stdin.readline

def main():
    n, m, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    B = [int(input()) for _ in range(m)]

    # 기존 창고의 물품 수가 더 많으면, 일단 1층 물품부터 m층 ~ 1층 순서로 채우고 본다...
    if sum(A) > sum(B):
        x = sum(B)
        y = 0

        for i in range(m-1, -1, -1):
            curr = B[i]
            for j in range(n):
                if A[j] == 0:
                    continue

                if curr - A[j] >= 0:
                    y += (i+j+2) * A[j]
                    curr -= A[j]
                    A[j] = 0
                else:
                    y += (i+j+2) * curr
                    A[j] -= curr
                    break
    else:
        # 새로운 창고가 더 크면 꼭대기층 물품부터 1층 ~ m층 순서로 채운다...
        x = sum(A)
        y = 0

        for i in range(n-1, -1, -1):
            curr = A[i]
            for j in range(m):
                if B[j] == 0:
                    continue

                if curr - B[j] > 0:
                    y += (i+j+2) * B[j]
                    curr -= B[j]
                    B[j] = 0
                else:
                    y += (i+j+2) * curr
                    B[j] -= curr
                    break
    
    print(x, y)


main()