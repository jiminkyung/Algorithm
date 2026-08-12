# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/92342


# 구현 연습하기 좋은 문제
def solution(n: int, info: list[int]) -> list[int]:
    ret = None
    max_diff = 0

    def dfs(curr: list[int], idx: int, cnt: int):
        nonlocal ret, max_diff

        # 화살을 다 썼거나, 모든 과녁을 체크했을경우.
        if cnt == 0 or idx == 11:
            curr[10] += cnt  # 남은 화살을 마지막 과녁에 몰빵

            # 점수 계산
            apeach_score = lion_score = 0
            for i in range(11):
                if info[i] == 0 and curr[i] == 0:  # 둘 다 0점일경우 넘어감
                    continue

                if info[i] >= curr[i]:
                    apeach_score += 10 - i
                else:
                    lion_score += 10 - i
            
            diff = lion_score - apeach_score
            
            # 기존 차이보다 더 크다면 갱신
            if diff > max_diff:
                max_diff = diff
                ret = curr[:]
            # 기존 차이와 같지만, 낮은 과녁을 더 많이 맞혔다면 갱신
            elif diff == max_diff and ret:
                if curr[::-1] > ret[::-1]:
                    ret = curr[:]

            # 몰빵했던 화살 회수
            curr[10] -= cnt
            return
        
        # 🗝️ 라이언이 쏘는 화살의 갯수는,
        # 1. 어피치를 이기던가 (어피치가 현재 과녁에 쏜 갯수 + 1)
        # 2. 지던가 (아예 안 쏨)
        # 둘 중 하나임.

        # 1. 현재 과녁에서 이길 수 있을 정도의 화살이 남아있을경우.
        if info[idx] + 1 <= cnt:
            curr[idx] = info[idx] + 1
            dfs(curr, idx+1, cnt - curr[idx])
            curr[idx] = 0
        # 2. 현재 과녁에서 이기지 않으려 하거나, 화살이 없을 경우.
        dfs(curr, idx+1, cnt)

        return


    dfs([0] * 11, 0, n)

    return ret if ret else [-1]