"""
카카오 3차 문제. 풀다가 정렬 부분에서 생각회로 고장+코드에러.
그리고 문제를 제대로 읽자!!! 마지막 TAIL부분 설명을 잘못봤는데, 이 병을 꼭 고쳐야겠다...
1. 도중에 포기한 코드(정렬부분은 제외함)
2. AI에게 도움받은 코드
3. 정답 코드 중 깔끔했던 코드(완전한 해답인지는 100% 확신할 수 없을듯.)
"""

# 1
import re

def solution(files):
    test = {}
    for i in range(len(files)):
        names = re.findall(r"([a-zA-Z-. ]+)([^0]?[0-9]+)(.*)?", files[i])
        test[i] = names

# 2
import re

def solution(files):
    def key_func(file):
        # [(요소들)] 의 형태로 반환하기 때문에 [0]으로 튜플만 선택해준다.
        head, number, tail = re.findall(r"([a-zA-Z-. ]+)(\d{1,5})(.*)?", file)[0]
        return (head.upper(), int(number))

    return sorted(files, key=key_func)

# 3
import re

def solution(files):
    # a: 리스트를 NUMBER 기준으로 정렬, b: a를 HEAD 기준으로 정렬.
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b