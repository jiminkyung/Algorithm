def solution(id_pw, db):
    id, pw = id_pw[0], id_pw[1]
    for i, p in db:
        if i == id:
            if p == pw:
                return "login"
            else:
                return "wrong pw"
    return "fail"