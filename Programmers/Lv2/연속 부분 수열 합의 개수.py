"""
원형수열이라고 가정한 문제. 파이널 팀 정할때 풀어봤던것같다...

첫번째 풀이는 mod를 사용한 풀이. 이전부분의 합을 재사용할수있다.
두번째 풀이는 슬라이싱을 사용한 풀이. sum을 매번 호출해야하며 재사용성이 떨어짐.
속도도 첫번째 풀이가 훨씬 빨랐다.
"""

# 👍 처음 코드.
def solution(elements):
    ret = set()
    length = len(elements)

    for i, element in enumerate(elements):
        curr = element
        ret.add(curr)

        for k in range(i+1, i+length):
            curr += elements[k%length]
            ret.add(curr)
    return len(ret)

# 슬라이싱을 이용한 코드로도 풀어봄.
def solution(elements):
    ret = set()
    length = len(elements)

    for size in range(1, length):
        for idx in range(length):
            if idx+size <= length:
                curr = sum(elements[idx: idx+size])
            else:
                curr = sum(elements[idx:]) + sum(elements[:idx+size-length])
            ret.add(curr)
    ret.add(sum(elements))

    return len(ret)