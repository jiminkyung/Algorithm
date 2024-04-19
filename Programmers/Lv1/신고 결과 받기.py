# 너무 더럽게 푼 것 같아서 마음에 안듦.

def solution(id_list, report, k):
    cnt = {ids: 0 for ids in id_list}
    sets = set(report)
    for s in sets:
        _, who = s.split()
        cnt[who] += 1
    ret = list(filter(lambda x: cnt[x] >= k, cnt))
    cnt2 = {ids: 0 for ids in id_list}
    for s in sets:
        user1, user2 = s.split()
        if user2 in ret:
            cnt2[user1] += 1
    return [cnt2[i] for i in cnt2]