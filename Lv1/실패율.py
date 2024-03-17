# 런타임 에러!
def solution(N, stages):
    n = [i for i in range(1, N+1)]
    cnt = [stages.count(i) for i in n]
    curr = len(stages)
    fail = []
    i = 0
    while i < N:
        fail.append((cnt[i] / curr, n[i]))
        curr -= cnt[i]
        i += 1
    sorted_ret = sorted(fail, key=lambda x: (-x[0], x[1]))
    ret = [i[1] for i in sorted_ret]
    return ret

# 다시 해보기.
# => 이것도 런타임 에러...
# => zero devision 에러가 문제였다.
def solution(N, stages):
    cnt = {i: stages.count(i) for i in range(1, N+1)}
    curr = len(stages)
    fail = {}
    i = 1
    while i <= N:
        if cnt[i] == 0:
            fail[i] = 0
        else:
            fail[i] = cnt[i] / curr
        curr -= cnt[i]
        i += 1
    return sorted(fail, key=lambda x: (-fail[x], x))