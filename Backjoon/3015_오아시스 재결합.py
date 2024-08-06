# 스택 2

# 참고: https://aquaplane-mode.tistory.com/59
# 메모리: 50548KB / 시간: 352ms

from sys import stdin


input = stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]

def acquiesce():
    #  (키, 연속하면서 동일한 키의 갯수)
    stack = []
    ret = 0

    for h in heights:
        while stack and stack[-1][0] < h:  # 스택이 존재하고 현재 사람이 직전 사람보다 클 때,
            ret += stack.pop()[1]  # 직전 사람을 꺼낸 후 키의 갯수를 결과값에 더해준다.

        if not stack:  # 스택이 비어있다면 (현재 사람의 키, 1) 추가
            stack.append((h, 1))
            continue

        # 스택이 비어있지 않다면,
        if stack[-1][0] == h:  # 직전 사람의 키가 현재 사람의 키와 같을 때,
            cnt = stack.pop()[1]  # 직전 사람을 꺼낸 후 키의 갯수를 결과값에 더해준다.
            ret += cnt

            if stack:  # 그래도 스택이 남아있는 경우 결과값에 1을 더해준다. (2, 1, 1)일때 (2, 1), (2, 1) 이므로.
                ret += 1
            
            stack.append((h, cnt+1))  # 그리고 (키, 기존 키의 갯수 + 1(현재 사람))을 스택에 추가.
        
        # 현재 사람의 키가 직전 사람의 키보다 작다면 그대로 스택에 추가 후 결과값에 1 추가.
        else:
            stack.append((h, 1))
            ret += 1
    
    return ret

print(acquiesce())