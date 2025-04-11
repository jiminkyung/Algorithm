# 수학


# 문제: https://www.acmicpc.net/problem/1112

"""
x % b 식에서 피제수는 x, 제수는 b를 말함.
진법변환을 하려면 x % b의 값이 항상 양수가 나와야함.
하지만 파이썬은 제수의 부호를 따름.

따라서 나머지가 양수로 나오게끔 만드려면 (x // b) + 1, (x % b) + |b| 를 해줘야함
ex) -10을 -4진법으로 변환
(처리 전)
    - 몫: -10 // -4 = 2
    - 나머지: -2
(양수 처리 후)
    - 몫: 2 + 1 = 3
    - 나머지: -2 + 4 = 2

확인해보면, -4 * 3 = -12이므로, -12 + 2 = 10이 됨.

그리고 질문글 중에 진법변환에 대해 자세히 설명해준 분이 계심! 헷갈릴때 보기 좋을듯.
링크👉 https://www.acmicpc.net/board/view/76104
"""

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    x, b = map(int, input().split())
    
    def convert(x, b) -> int:
        if x == 0 or b == 0:
            return 0
        
        # 1. 양의 진법으로 변환할경우
        if b > 0:
            is_negative = bool(x < 0)  # 변환시킬 수 x가 음수인지 체크
            x = abs(x)
            ret = ""

            while x:
                ret = str(x % b) + ret
                x //= b
            
            return "-" + ret if is_negative else ret  # x가 음수라면 앞에 - 부호를 붙여준 뒤 반환
        # 2. 음의 진법으로 변환할경우
        else:
            ret = ""

            while x:
                remain = x % b
                x //= b

                if remain < 0:
                    remain += abs(b)
                    x += 1
                
                ret = str(remain) + ret
            
            return ret
    
    print(convert(x, b))


main()