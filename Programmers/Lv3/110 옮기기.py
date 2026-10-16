# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/77886


# 다시 풀어볼만한 문제
# 참고한 글... https://school.programmers.co.kr/questions/93438
def solution(s: list[str]) -> list[str]:
    total = []

    for i in range(len(s)):
        # 마지막 3글자가 "110"일경우, stack에서 지운 후 카운트 +1
        word = s[i]
        stack = ""
        cnt = 0

        for i in range(len(word)):
            stack += word[i]

            if len(stack) >= 3 and stack[-3:] == "110":
                stack = stack[:-3]
                cnt += 1

        # "11"이 나오는 지점을 찾고, 그 앞에 "110"군집을 삽입
        # -> stack에는 "110"이 없는 상태이므로, "11"이 나온다면 뒤에는 무조건 "1"이 나오거나, 아무것도 없을것임.
        idx = stack.find("11")
        group = "110" * cnt  # "110" 군집
        ret = None

        # 만약 "11"이 없다면?

        # 1. stack이 존재하지 않는 경우 (s에 110 덩어리만 존재할경우)
        # -> group 자체를 ret으로 저장.
        # 2. stack의 마지막 글자가 "1"일 경우
        # -> 마지막 "1" 앞에 group 삽입. "1" "110" 보다는 "110" "1" 이 사전순으로 더 앞서니까...
        # 3. 마지막 글자가 "0"이라면
        # -> 그냥 그 뒤에 group 삽입.
        if idx == -1:
            if not stack:
                ret = group
            elif stack[-1] == "1":
                ret = stack[:-1] + group + "1"
            else:
                ret = stack + group
        else:
            # "11"이 존재할경우, 해당 위치 앞에 group 삽입.
            # 모든 "110"들은 group으로 빠진 상태이므로, stack의 "11"은 "11", 또는 "111..."임.
            # 따라서 "110"을 "11"앞에 넣어줘야 사전순으로 앞서게 됨.
            ret = stack[:idx] + group + stack[idx:]
    
        total.append(ret)
    
    return total