# 정렬
# 이분 탐색


# 문제: https://www.acmicpc.net/problem/2428

# 이분탐색으로 풀었지만, 투 포인터로 푸는게 훨씬 효율적이다.
# for문으로 i를 증가시키며, while문으로 files[i] * 0.9 > files[j] 를 만족할때까지 j를 증가시킨다.
# -> while문이 끝난 후 j값은 "표절 검사를 해야하는 파일 중 가장 작은값(의 인덱스)"를 의미하게 된다.

# 1) 이분탐색 X, 포인터만 사용
# 참고👉 https://www.acmicpc.net/source/92176535
# 메모리: 44748KB / 시간: 104ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    files = list(map(int, input().split()))
    files.sort()

    ret = 0
    idx = 0

    for i in range(N):
        # i보다 작은 파일 중 검사 대상에 해당되는 파일(의 시작인덱스)
        # i = 10이고 idx = 7이라면 3쌍을 검사해야함
        while files[idx] < 0.9 * files[i]:
            idx += 1
        ret += i - idx
    
    print(ret)


main()


# 2) 이분탐색 사용
# 메모리: 44748KB / 시간: 324ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    files = list(map(int, input().split()))
    files.sort()
    
    ret = 0

    def binary_search(start, target):
        end = N-1
        idx = N
        # idx: 표절 검사가 필요 없는 크기의 파일 중 가장 작은값의 인덱스
        # Fi >= Fj * 0.9일때만 검사해야 하니 10 * Fi < Fj * 9이면 Fj는 표절 검사를 하지 않아도 됨.

        while start <= end:
            mid = (start + end) // 2

            if files[mid] * 9 > target:
                idx = mid
                end = mid - 1
            else:
                start = mid + 1
        return idx-1
    
    for i in range(N-1):
        idx = binary_search(i+1, files[i] * 10)
        ret += idx - i
    
    print(ret)


main()