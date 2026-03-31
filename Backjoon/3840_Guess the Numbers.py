# 문자열
# 브루트포스 알고리즘
# 파싱


# 문제: https://www.acmicpc.net/problem/3840

# 처음엔 스택을 써야하나? 싶었는데, 주어지는 값의 형태가 무조건 (미지수 연산자 미지수)형태이므로, 재귀가 더 어울림.
# 나중에 다시 풀어볼만한 문제. 연습하기 좋을듯.

# 메모리: 33432KB / 시간: 332ms
from sys import stdin
from itertools import permutations


def main():
    data = stdin.read().splitlines()[:-1]  # 마지막 (0 0) 데이터는 제외

    for i in range(0, len(data), 2):
        nums = list(map(int, data[i].split()))  # 미지수 관련 데이터
        formula = data[i+1]  # 공식

        print(solve(nums, formula))


def solve(nums: list[int], formula: str) -> str:
    # 미지수 하나만 존재하는 공식이라면 바로 YES 반환.
    if formula == "a":
        return "YES"

    def parsing(mapping: dict[str: int]) -> int:
        nonlocal pos  # formula 인덱스

        # 현재 위치 값이 미지수라면, 맵핑 데이터에 해당되는 정수 값을 반환.
        if formula[pos].isalpha():
            num = mapping[formula[pos]]
            pos += 1
            return num
        
        # 괄호라면 트리 구조로 왼쪽, 오른쪽 값을 구한 후 연산자에 맞게 계산.
        if formula[pos] == "(":
            pos += 1
            left = parsing(mapping)
            op = formula[pos]  # left 처리하면서 pos가 갱신된 상태임
            pos += 1
            right = parsing(mapping)
            pos += 1  # ) 패스

            val = 0

            if op == "+":
                val = left + right
            elif op == "-":
                val = left - right
            else:
                val = left * right
        return val
    

    cnt = nums[0]  # 미지수 갯수
    target = nums[-1]  # 도출되어야 하는 값
    alp = [f for f in formula if f.isalpha()]
    perms = permutations(nums[1:-1], cnt)

    # 순열 생성 후 파싱+계산을 통해 얻은 값을 타겟값과 비교.
    for perm in perms:
        # 인덱스로 관리하기보단 처음부터 맵핑시켜주는게 편함.
        mapping = {alp[i]: perm[i] for i in range(cnt)}
        pos = 0

        ret = parsing(mapping)

        if ret == target:
            return "YES"
    return "NO"


main()