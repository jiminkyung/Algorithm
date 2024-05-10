"""
itertools 모듈을 불러와서 풀려 했지만, 좋은 풀이가 있길래 가져왔다.

dic: 알파벳 모음을 순서대로 저장한 리스트.
li: 각 자리의 알파벳이 사전 순서에 기여하는 값을 저장한 리스트.
"""

def solution(word):
    answer = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    li = [5**i for i in range(len(dic))]
    
    for i in range(len(word)-1,-1,-1):
        idx = dic.index(word[i])
        for j in range(5-i):
            answer += li[j]*idx
        answer+=1
    return answer