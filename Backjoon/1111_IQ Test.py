# 수학


# 문제: https://www.acmicpc.net/problem/1111

# 주어진 수가 1 or 2개일경우, n1 != n2라면 A 반환.
# 연립방정식을 사용하여 a, b를 구한 뒤, 나머지 식에 대입해보고 틀리면 B 반환.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))

    def calc(N: int, nums: list) -> int:
        # 수가 1개 혹은 2개만 주어진다면, 여러개의 답이 나올 가능성이 있음.
        if N == 1:
            return "A"

        if N == 2:
            if nums[0] == nums[1]:  # 🚨 만약 n1 = n2일경우, a: 1, b: 0이 가능함.
                return nums[0]
            return "A"

        a = b = None

        x1, x2, x3 = nums[:3]

        # x2 = x1 * a + b
        # x3 = x2 * a + b
        # 연립방정식으로,
        # x3 - x2 = (x2 - x1) * a

        # a = (x3 - x2) // (x2 - x1)
        # b = x2 - x1 * a
        if (x2 - x1) == 0:
            # 마찬가지로 n1 = n2 = n3...라면 a: 1, b: 0으로 가능
            if x3 == x2:
                a, b = 1, 0
            else:
                return "B"
        else:
            if (x3 - x2) % (x2 - x1) != 0:
                return "B"
            a = (x3 - x2) // (x2 - x1)
            b = x2 - x1 * a

        for i in range(N-1):
            if nums[i] * a + b != nums[i+1]:
                return "B"

        return nums[-1] * a + b
    
    print(calc(N, nums))


main()