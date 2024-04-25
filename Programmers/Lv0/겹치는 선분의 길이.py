def solution(lines):
    test = []
    for p1, p2 in lines:
        test.append(set([x for x in range(p1, p2)]))
    ret = test[0] & test[1] | test[1] & test[2] | test[2] & test[0]

    return len(ret)

# 훨씬 깔끔한 코드. 마지막 합집합 부분은 이 코드를 참고했다 ㅎ
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])