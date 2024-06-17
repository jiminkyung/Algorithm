# 정렬
# 해당 좌표값보다 작은 좌표값들의 개수를 출력하면 되는 문제.


# 첫번째 코드. 시간초과. 예상하긴 했다...
import sys

input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))
set_nums = list(set(nums))

set_nums.sort()

ret = [set_nums.index(n) for n in nums]
print(*ret)


# 다시 시도해보기. 역시 웬만한 시간초과의 해결책은 딕셔너리인듯싶다.
# 메모리: 155276KB / 시간: 1976ms
# 참고 👉 https://gudwns1243.tistory.com/52
import sys

input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))
set_nums = sorted(list(set(nums)))

ret = {set_nums[i]: i for i in range(len(set_nums))}

for n in nums:
    print(ret[n], end=" ")


# 숏코딩 최강자 ㅋㅋ
*a,=map(int,[*open(0)][1].split())
d=dict(zip(sorted({*a}),range(9**9)))
print(*[d[i]for i in a])