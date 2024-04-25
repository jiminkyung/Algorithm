def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for word in words:
            i = i.replace(word, " ")
        i = i.replace(" ", "")
        if not len(i):
            cnt += 1
    return cnt

"""
순열 함수 from itertools import permutations를 이용한 풀이!
처음 보는 모듈인데 알아봐야겠다 ㅎㅎ
👉 https://velog.io/@sugyeonghh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%AC%B8-%EC%98%B9%EC%95%8C%EC%9D%B41Python
"""

# re 를 이용한 풀이. 제일 깔끔하다.
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt

"""
내가 풀이에 참고했던 코드 👉 https://harami.tistory.com/20
아이고 ㅎㅎ 난 아직 멀었다...
"""