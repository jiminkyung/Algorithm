# 수학
# 정렬
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1448
# 메모리: 77292KB / 시간: 560ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # 내림차순으로 정렬
    straws = [int(input()) for _ in range(N)]
    straws.sort(reverse=True)
    ret = -1

    for i in range(N-2):
        # 3개씩 선택하고 "가장 긴 빨대 < 나머지 두 빨대"를 만족하면 break
        l1, l2, l3 = straws[i:i+3]

        if l2 + l3 > l1:
            ret = l1 + l2 + l3
            break
    
    print(ret)


main()


# 메모리 사용량이 절반인 코드!
# 출처👉 https://www.acmicpc.net/source/74403972

# 100000부터 1까지 순회하면서, 해당 길이의 갯수가 1 이상이라면 selected에 추가.
# selected의 갯수가 2개가 되면, 현재 검사중인 숫자 i와 selected의 두 수를 가지고 비교함.
# 긴변 < 두변의 합 을 만족하지 못한다면 제일 긴 변을 selected에서 pop.
import sys

input = sys.stdin.readline
n = int(input())
num = [0] * (1000001)
for _ in range(n):
    num[int(input())] += 1

selected = []

i = 1000000
while i > 0:
    if not num[i]:
        i -= 1
        continue

    elif len(selected) <= 1:
        selected.append(i)
        num[i] -= 1
        continue

    elif selected[0] >= selected[1] + i:
        selected.pop(0)
        continue

    else:
        print(sum(selected) + i)
        exit()

print(-1)