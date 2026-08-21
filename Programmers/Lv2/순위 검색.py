# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72412


# 처음 시도한 방법) 조건을 세분화해서 이중 리스트로 저장함. (level[lv] = [지원자 임시 번호들], score[i] = i번째 지원자의 점수)
# 각 세부 조건에 맞는 리스트를 set화 시키고, and 연산을 통해 지원자들을 추림. -> 추려진 지원자들의 점수 확인.
# => 정확성 테스트는 통과했으나 효율성 테스트에서 실패함.

# 점수 X를 제외하고, 세부 조건은 4개뿐임. 4개 조건마다 (조건, -)을 선택해 모든 조합 생성.
# conditions[조합] = [조합에 해당되는 지원자들의 점수] 형태로 관리하고, 특정 점수 이상이 몇명인지는 이분탐색을 통해 계산.
def solution(info: list[str], query: list[str]) -> int:

    def binary_search(target: int, scores: list[int]) -> int:
        """ target 이상인 첫 번째 위치를 찾는 이분탐색 함수 """
        start, end = 0, len(scores) - 1

        while start <= end:
            mid = (start + end) // 2

            if scores[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        
        return start


    def check(q: str) -> int:
        q = q.replace(" and ", " ")
        *condition, score = q.split()
        condition = " ".join(condition)
        score = int(score)

        scores = conditions.get(condition, 0)

        # 조건에 해당되는 사람이 없을경우 바로 0 반환.
        if scores == 0:
            return 0
        
        # 조건에 해당하고, 점수가 score 이상인 첫 번째 위치.
        idx = binary_search(score, scores)

        return len(scores) - idx

    
    conditions = {}

    for i in range(len(info)):
        lang, stack, level, food, score = info[i].split()
        score = int(score)

        # (조건, -) 중 택일하는 방식으로 순회.
        for l in (lang, "-"):
            for s in (stack, "-"):
                for lv in (level, "-"):
                    for f in (food, "-"):
                        comb = " ".join((l, s, lv, f))
                        conditions.setdefault(comb, []).append(score)
    
    # 저장된 점수를 오름차순으로 정렬.
    for key in conditions.keys():
        conditions[key].sort()
    
    ret = []
    for q in query:
        ret.append(check(q))
    
    return ret