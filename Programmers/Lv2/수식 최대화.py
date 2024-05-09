"""
첫번째 풀이는 내 코드+클로드 풀이.
숫자는 nums, 연산자는 ops에 각각 저장. => nums[i], nums[i+1]은 ops[i]와 연관되어있음.
순열을 이용해 각 우선순위대로 계산 후 max값을 반환.
"""

# 내 코드+클로드 풀이
from itertools import permutations

def solution(expression: str) -> int:
    # 수식을 파싱하여 숫자와 연산자 분리
    nums = []
    ops = []
    tmp = ""
    for char in expression:
        if char.isdigit():
            tmp += char
        else:
            nums.append(int(tmp))
            ops.append(char)
            tmp = ""
    nums.append(int(tmp))

    # 연산자 우선순위 조합 생성
    priorities = list(permutations(set(ops)))

    # 각 우선순위 조합에 대해 계산 수행
    answer = 0
    for priority in priorities:
        num_copy = nums[:]
        op_copy = ops[:]
        for op in priority:
            while op in op_copy:
                idx = op_copy.index(op)
                if op == "+":
                    num_copy[idx] += num_copy[idx+1]
                elif op == "-":
                    num_copy[idx] -= num_copy[idx+1]
                else:
                    num_copy[idx] *= num_copy[idx+1]
                num_copy.pop(idx+1)
                op_copy.pop(idx)
        answer = max(answer, abs(num_copy[0]))

    return answer

# 정답 풀이 중 좋아요가 가장 많았던 풀이. 간결하지만 eval()은 지양하는게 좋다.
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)