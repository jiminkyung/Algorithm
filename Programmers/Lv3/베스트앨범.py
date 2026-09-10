# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres: list[str], plays: list[int]) -> list[int]:
    # 장르별로 딕셔너리에 저장. dic[장르]: [(-재생횟수, 고유번호), ...]
    dic = {}
    N = len(genres)

    for i in range(N):
        dic.setdefault(genres[i], []).append((-plays[i], i))
    
    # 재생횟수를 기준으로 장르를 내림차순 정렬 (sum값이 음수)
    sorted_genres = sorted(dic, key=lambda x: sum(t for t, _ in dic[x]))
    ret = []

    for genre in sorted_genres:
        # 재생횟수가 큰 값, 고유번호가 낮은 값으로 정렬 후 두 개만 추림
        val = sorted(dic[genre])[:2]
        ret.extend(num for _, num in val)
    
    return ret