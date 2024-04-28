"""
이 문제는 ../Programmers/Lv2/주식가격.py 의 문제를 변형한것이다.
풀이는 예시 답안으로 소개했던 두번째 풀이와 같다.


🟢 날짜별로 측정한 온도가 주어졌을 때, 각 날짜에 대해 며칠 동안 온도가 내려가지 않는지 계산하는 함수를 작성하세요.

입력:
- temperatures: 날짜별 온도가 기록된 정수 배열

출력:
- 각 날짜에 대해 온도가 내려가지 않는 기간을 저장한 정수 배열

예시:
- 입력: [30, 32, 32, 30, 33, 31, 30]
- 출력: [6, 2, 1, 3, 1, 1, 0]
"""

def solution(temperatures):
    stack = [] # 스택 생성
    length = len(temperatures)
    ret = [0] * length # 반환할 리스트 ret 생성. 길이는 temperatures의 길이만큼.

    for i in range(length):
        if stack: # 스택이 비어있지 않다면
            while stack and stack[-1][1] > temperatures[i]: # 스택이 비어있지 않고, 스택의 가장 위의 값(마지막 값)의 온도가 현재 온도보다 크다면. 즉, 온도가 내려갔다면.
                idx, _ = stack.pop() # 스택의 마지막 값을 꺼낸다. 스택의 각 요소는 [인덱스, 온도]의 형태로 저장되어있으므로 idx, _로 뽑아준다. 온도값은 필요 X.
                ret[idx] = i - idx # (현재 인덱스값 - 스택의 인덱스값)을 ret의 idx번째 인덱스에 넣어준다. 스택에 해당되는 온도의 유지기간을 저장하는것.
        stack.append([i, temperatures[i]]) # i = 0 이거나 온도 유지 or 상승일경우 스택에 [인덱스, 온도]를 추가해준다.
    for i, _ in stack: # 처음부터 끝까지 온도 유지 or 상승인 경우
        ret[i] = (length - 1) - i # (temperatures의 길이-1)을 한 값에서 해당 온도의 인덱스값을 빼준다. -1을 한 이유는 인덱스는 0부터 시작하기 때문.
    return ret

print(solution([30, 32, 32, 30, 33, 31, 30]))