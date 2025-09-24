# 이분 탐색


# 문제: https://www.acmicpc.net/problem/2343

"""
'이분탐색' 키워드를 보고도 헷갈렸던 문제. 나중에 다시 풀어봐야 함.
이분탐색은 두 부분에 적용할 수 있음.
1. 블루레이의 크기
    - 모든 영상 중 가장 큰 값을 start로 지정. (M개의 블루레이는 모두 같은 크기여야하기 때문)
    - end는 주어진 최댓값 10,000을 N만큼 곱한 값.
2. 블루레이의 크기(target)만큼 나눈 갯수가 M개 이하인지 체크할 때.
    - 누적합을 구한 다음, 각 구간의 끝부분을 이분탐색으로 구한다.
    - 예제로 보면, target=17일때 첫번째 구간은 [1, 2, 3, 4, 5]. 여기까지의 합은 15. 마지막 인덱스는 4.
    - 다음 target을 17 + 15 = 32로 지정한다음 5번 인덱스부터 다시 누적합 체크. S[i]가 32 이하일때 마지막 인덱스 저장.
    - ...반복...

이분탐색을 2번처럼 적용하는건 생각 못했다. 많이 배워감.

🚨그리고 주의해야 할 점이 있다. 꼭 M개의 블루레이 모두에 영상을 녹화할 필요는 없다.
즉 특정한 크기 X만큼 녹화했을때 M개 이하로 나누어지기만 하면 됨.
[1, 1, 1, 1, 1, 1, 1, 1] 이고 M이 7이라면 최솟값은 2가 되겠다.
"""

# 1) 블루레이의 크기에만 이분탐색 적용
# 메모리: 42168KB / 시간: 324ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    length = list(map(int, input().split()))

    def calc(target: int) -> int:
        cnt = 1  # 1개로 시작
        curr = 0

        for i in range(N):
            if curr + length[i] > target:
                cnt += 1
                curr = length[i]
            else:
                curr += length[i]
        
        return cnt


    def binary_search() -> int:
        start, end = max(length), 10000 * N
        ret = -1

        while start <= end:
            mid = (start + end) // 2

            cnt = calc(mid)
            # 갯수가 M개 이하일때 ret 갱신
            if cnt > M:
                start = mid + 1
            else:
                end = mid - 1
                ret = mid
        
        return ret


    print(binary_search())


main()


# 2) 블루레이 크기 + 갯수 확인에 모두 이분탐색 적용
# 메모리: 42168KB / 시간: 108ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    length = list(map(int, input().split()))
    S = length[:]  # length의 누적합 리스트
    
    for i in range(1, N):
        S[i] += S[i-1]

    def calc(target: int) -> int:
        cnt = start = 0

        # start: 현재 구간의 시작 인덱스
        while start < N:
            # 현재 목표값: 이전 구간의 합 + 목표값
            target_sum = (S[start-1] if start > 0 else 0) + target

            left, right = start, N-1
            end_idx = start

            while left <= right:
                mid = (left + right) // 2

                if S[mid] <= target_sum:
                    end_idx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            cnt += 1
            start = end_idx + 1  # 다음 시작점

        return cnt


    def binary_search() -> int:
        # start는 가장 큰 길이값으로, end는 최대값 * N으로 지정.
        # -> [1, 2, 10]일 경우 M이 3 이상이어도 블루레이 하나당 크기가 10은 되어야함. start를 1로 잡아도 상관없긴 하다.
        start, end = max(length), 10000 * N
        ret = -1

        while start <= end:
            mid = (start + end) // 2
            # 블루레이 크기는 mid로 잡았을때 나오는 갯수
            cnt = calc(mid)
            # M보다 크다면 증가
            if cnt > M:
                start = mid + 1
            # M 이하라면 mid값 저장 후 크기를 더 줄여봄
            else:
                end = mid - 1
                ret = mid
        
        return ret

    print(binary_search())


main()