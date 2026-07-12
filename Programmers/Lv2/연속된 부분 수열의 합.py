# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence: list, k: int):
    l = len(sequence)
    ret = (0, l)
    left = right = 0
    curr = sequence[0]

    while right < l and left <= right:
        if curr == k:
            # 현재 구간 길이가 이전 결과값보다 짧다면 갱신
            if (ret[1] - ret[0] + 1) > (right - left + 1):
                ret = (left, right)
            curr -= sequence[left]
            left += 1
            right += 1
            if right < l:
                curr += sequence[right]
        elif curr > k:
            curr -= sequence[left]
            left += 1
        else:
            right += 1
            if right < l:
                curr += sequence[right]
    return ret