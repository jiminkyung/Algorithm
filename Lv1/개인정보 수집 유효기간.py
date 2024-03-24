def solution(today, terms, privacies):
    t = {term.split()[0]: int(term.split()[1])*28 for term in terms}
    ret = []
    def dates(s):
        y, m, d = s.split(".")
        return [int(y), int(m), int(d)]
    today = dates(today)
    for i, p in enumerate(privacies, start=1):
        date, val = p.split()
        date = dates(date)
        d = (today[0]-date[0])*12*28 + (today[1]-date[1])*28 + (today[2]-date[2])
        if d >= t[val]:
            ret.append(i)
    return ret

# 아래는 다른 사람의 풀이. 나도 map쓸걸.
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire