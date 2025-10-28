# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2777
# 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        # N의 한자릿수 약수 후보들
        # nums에 저장된 숫자들을 서로 곱하면 N이 되는거임.
        nums = []

        # N이 i로 나누어지면 nums에 추가
        for i in range(2, 10):
            while N % i == 0:
                nums.append(i)
                N //= i
        
        # N을 (한자릿수*한자릿수)형태로 쪼갤 수 없다면 -1 출력
        if N != 1:
            print(-1)
            continue

        nums.sort()
        ret = 1  # 마지막에 남아있는 curr도 추가해야함. 미리 추가.

        idx = 0
        curr = 1
        while idx < len(nums):
            # curr과 nums[idx]를 곱한 값이 한자릿수라면, curr에 nums[idx]를 곱해준다.
            # -> 자릿수를 최대한 줄이기 위함
            if (curr * nums[idx]) // 10 == 0:
                curr *= nums[idx]
            # 아니라면 자릿수를 +1 카운트 한 뒤 curr값을 nums[idx]로 저장.
            # ex) curr = 4, nums[idx] = 3이면 12이므로 43으로 적어야 가능해짐.
            # -> 43이든 34든 자릿수는 같음. 자릿수만 신경쓰면 됨.
            else:
                ret += 1
                curr = nums[idx]
            idx += 1
        
        print(ret)


main()