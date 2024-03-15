def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zeros = lottos.count(0)
    if not cnt and zeros:
        return [7-zeros, 6]
    elif not zeros and not cnt:
        return [6, 6]
    else:
        return [(7-cnt)-zeros, 7-cnt]

# testcase 14번에서 막혔는데 반례는 아래와 같았다.
print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))

# rank를 이용한 풀이. 우와!
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]