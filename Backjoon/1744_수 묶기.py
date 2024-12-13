# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/1744
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
ret = 0

minus = []
plus = []
zero = 0
one = 0

for n in nums:
    if n < 0:
        minus.append(n)
    elif n == 0:
        zero += 1
    elif n == 1:
        one += 1
    else:
        plus.append(n)

"""
1. 음수값 처리
- 짝수개 존재할경우: 순서대로 두개씩 곱해줌
- 하나만 존재할경우:
    - 0이 있을경우: 0과 곱해줘서 0으로 만들어준 뒤 0갯수는 감소시킨다.
    - 없을경우: 그대로 더해줌
- 홀수개 존재할경우: 제일 큰값(양수에 가까운 값)을 제외하고 작은값부터 두개씩 곱해줌
    - 0이 있을경우: 위에서 남겨둔 제일 큰값과 곱해 0으로 만들어준 뒤 0갯수 감소.
    - 없을경우: 그대로 더해줌
"""
if minus:
    if len(minus) % 2 == 0:
        for i in range(0, len(minus), 2):
            ret += minus[i] * minus[i+1]
    elif len(minus) == 1:
        if zero > 0:
            zero -= 1
        else:
            ret += minus[0]
    else:
        for i in range(0, len(minus)-1, 2):
            ret += minus[i] * minus[i+1]
        if zero > 0:
            zero -= 1
        else:
            ret += minus[-1]

"""
2. 양수값 처리
- 짝수개 존재할경우: 순서대로 두개씩 곱해줌
- 홀수개 존재할경우: 제일 작은값을 제외하고 큰값부터 두개씩 곱해줌.
    - 제일 작은값은 그대로 더해준다.
    - 0은 양수값 처리시 사용하지 않기 때문에, 1개만 존재할경우를 따로 체크할 필요 없음.
"""
if plus:
    if len(plus) % 2 == 0:
        for i in range(0, len(plus), 2):
            ret += plus[i] * plus[i+1]
    else:
        for i in range(len(plus)-1, 0, -2):
            ret += plus[i] * plus[i-1]
        ret += plus[0]

"""
3. 결과값 출력
- 1, 2 과정을 거친 ret에 1의 갯수만큼을 더해준 값이 결과값이 됨.
"""
print(ret + one)