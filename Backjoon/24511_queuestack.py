# 스택, 큐, 덱
# 메모리: 54872KB / 시간: 184ms

from collections import deque
from sys import stdin


input = stdin.readline

N = int(input())

qs = zip(map(int, input().split()), map(int, input().split()))
dq = deque([element for i, element in qs if not i])

_ = input()
ret = []

new_elements = list(map(int, input().split()))

if sum(new_elements) == N:
    print(*new_elements)
else:
    for n in new_elements:
        dq.appendleft(n)
        ret.append(dq.pop())
    print(*ret)


# 좀 더 빠르게 구현해보기 1 - 동작까지는 구현해놓은 버전
# N, M은 입력만 받고 무시해버린다.
from collections import deque
from sys import stdin


input = stdin.readline
input()

# 큐에 해당하는 요소만 선택하여 역순으로 저장
dq = deque(y for x, y in zip(input().split(), input().split()) if x == "0")[::-1]
input()

# dq.appendleft()는 항상 None으로 처리되므로, dq.pop()이 실행된다. (x1 or x2 일때 x1이 False면 x2까지 실행되므로.)
# 따라서 매번 dq.appendleft(n)과 dq.pop()이 실행되는 셈이다.
print(*[dq.appendleft(n) or dq.pop() for n in input().split()])


# 좀 더 빠르게 구현해보기 2 - 과정 생략 후 원리만 이용한 버전
# 메모리: 47968KB / 시간: 140ms
# 생각외로 큰 차이는 없는듯하다.
from collections import deque
from sys import stdin


input = stdin.readline

input()

# 큐에 해당하는 요소만 선택하여 역순으로 저장
a = [y for x, y in zip(input().split(), input().split()) if x == "0"][::-1]

m = int(input())
a.extend(input().split())  # 여러번 append하지 않아도 됨.

# m개의 요소만 출력
print(*a[:m])