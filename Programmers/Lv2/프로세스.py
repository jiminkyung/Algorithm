def solution(priorities, location):
    orders = [(i, p) for i, p in enumerate(priorities)]
    ret = 0

    while True:
        curr = orders.pop(0)
        if any(curr[1] < o[1] for o in orders):
            orders.append(curr)
        else:
            ret += 1
            if curr[0] == location:
                return ret