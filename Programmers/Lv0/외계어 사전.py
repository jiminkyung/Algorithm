def solution(spell, dic):
    for s in dic:
        if set(s) == set(spell):
            return 1
    return 2

# 생각해보니 문제가 있는 코드다.
# 한번씩만 사용해야하는데 그 이상이 될수도 있다.
# 아래와 같이 수정해야 맞지 않나?... 어쨌든 테스트케이스에선 모두 통과되긴 했다.
def solution(spell, dic):
    for s in dic:
        if set(s) == set(spell) and len(s) == len(spell):
            return 1
    return 2