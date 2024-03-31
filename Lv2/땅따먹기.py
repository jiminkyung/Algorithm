# 첫번째 풀이 장렬히 탈락 ㅋㅋ
def solution(land):
    idx = land[0].index(max(land[0]))
    path = [idx]
    score = max(land[0])

    for row in range(1, len(land)):
        land[row][idx] = -1
        m = max(land[row])
        score += m
        idx = land[row].index(m)
        path.append(idx)
    return score

# 질문페이지에 가보니 dp로 풀라는 얘기가 많았다.
# 당연히 피보나치 수열 기초밖에 몰랐던 난 gpt에게 물어볼수밖에 없었다... too sad story.
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 현재 칸에 이전 행에서 자신을 제외한 칸들의 최대값을 더함
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

# 이전 행에서 현재 열을 제외한 최댓값을 구한다는 건 알았지만, 식을 어떻게 풀어야 할지 헤맸었다.
# 그리고 아래는 반례. 답은 20이 나와야 한다. 당연히 첫번째 방식으로는 불가능하다.
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))