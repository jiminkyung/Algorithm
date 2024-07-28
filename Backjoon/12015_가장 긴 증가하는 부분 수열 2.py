# 이분 탐색

"""
전에 발견했던 스택을 활용한 풀이를 떠올려보자. (11053번)
원소 값들은 같지 않지만, 길이는 정확하게 구할 수 있었다.
이걸 활용해서 풀어야 한다.

LIS의 가장 마지막 값보다 크다면 그대로 추가,
아니라면 binary_search(해당 원소값=target)을 실행한다.
현재 LIS안에서 target값으로 변경할만한 값의 위치를 찾아주는것이다.
- start는 0, end는 현재까지의 LIS길이-1 로 설정한다.
- start=end 가 될때까지 반복. 만약 LIS[mid]가 target보다 작다면 => start를 mid+1로 변경.
- LIS[mid]가 target보다 크거나 같다면 => end를 mid로 변경.
그러면 위치(인덱스)를 알 수 있고, 그대로 LIS[찾은 인덱스] = target 으로 변경해준다.
"""

# 메모리: 143264KB / 시간: 2176ms

from sys import stdin


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

def binary_search(target):
    start, end = 0, len(LIS)-1

    while start < end:
        mid = (start + end) // 2

        if LIS[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start

for a in A:
    if LIS[-1] < a:
        LIS.append(a)
    else:
        idx = binary_search(a)
        LIS[idx] = a

print(len(LIS))


# bisect 모듈을 활용할수도 있다. bisect_left(list, x): list에 x가 들어갈 가장 왼쪽 인덱스 반환
# 메모리: 145332KB / 시간: 948ms
from sys import stdin
from bisect import bisect_left


input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for a in A:
    if LIS[-1] < a:
        LIS.append(a)
    else:
        idx = bisect_left(LIS, a)
        LIS[idx] = a

print(len(LIS))