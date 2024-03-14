def solution(X, Y):
    same = sorted((set(X) & set(Y)), reverse=True)
    if not same:
        return "-1"
    elif same == ["0"]:
        return "0"

    ret = ""
    for i in same:
        x1 = X.count(i)
        y1 = Y.count(i)
        m = min(x1, y1)
        ret += i*m
    return ret