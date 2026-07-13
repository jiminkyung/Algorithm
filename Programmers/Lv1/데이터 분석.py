# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    mapping = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    v = mapping[ext]
    s = mapping[sort_by]
    
    ret = []
    
    # val_ext 값보다 작은 값만 추리기.
    for d in data:
        if d[v] < val_ext:
            ret.append(d)
    
    # sort_by 기준으로 오름차순 정렬
    ret.sort(key=lambda x: x[s])
    
    return ret