def solution(rank, attendance):
    available = list(filter(lambda x: attendance[rank.index(x)], rank))
    ret = sorted(available)[:3]
    func = lambda x: rank.index(x)
    s1, s2, s3 = func(ret[0]), func(ret[1]), func(ret[2])
    return 10000 * s1 + 100 * s2 + s3

# 깔끔하긴 하지만 가독성이 떨어지는 코드. But enumerate을 쓰는 좋은 방법.
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]