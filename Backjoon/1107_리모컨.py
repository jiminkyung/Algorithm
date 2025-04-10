# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1107

# 단순 반복&계산으로도 충분히 풀 수 있는 문제다.
# 하지만 맞은 풀이들을 보니 최적화 유무의 차이가 컸다!


# 1) 처음 풀이
# 주어진 채널번호 N을 기준으로 위/아래 번호들을 체크.
# 메모리: 32412KB / 시간: 708ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    M = int(input())

    # 망가진 버튼이 없을경우 대비
    broken = set()
    if M > 0:
        broken = set(input().rstrip())

    # +- 버튼으로만 이동했을시
    min_cnt = abs(100 - N)

    # 만약 단순이동값이 1 이하라면 그대로 출력 후 종료
    if min_cnt <= 1:
        print(min_cnt)
        return
    
    # 아니라면 N보다 큰 수, 작은 수들을 탐색한다.
    # 만약 탐색 중 모두 누를 수 있는 번호들만 존재할경우, 최솟값 갱신 후 종료.
    for i in range(min_cnt):
        up = str(N + i)
        cnt = len(up) + i  # 번호 누름 횟수 + 조작버튼 누름 횟수
        
        if cnt >= min_cnt:  # 기존 최솟값 이상일경우 break
            break

        if broken - set(up) == broken:
            min_cnt = min(cnt, min_cnt)
            break
    
    for i in range(min_cnt):
        down = str(N - i)
        cnt = len(down) + i

        if cnt >= min_cnt:
            break

        if broken - set(down) == broken:
            min_cnt = min(cnt, min_cnt)
            break
    

    print(min_cnt)


main()


# 2) 최적화 시도 풀이
# 아래의 풀이들을 보고 시도해봤다.
# 참고 1: https://www.acmicpc.net/source/67879472 (재귀)
# 참고 2: https://www.acmicpc.net/source/84770724 (자바느낌)

# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    M = int(input())

    broken = set()
    if M > 0:
        broken = set(map(int, input().split()))
    
    ret = abs(100 - N)

    # 단순조작 횟수가 1 이하 or 모든 버튼이 고장 or N이 102라면
    # 102의 경우 버튼을 직접 누르면 3회, 단순조작으로는 2회만으로 가능하다. 예외 케이스인셈.
    if ret <= 1 or M == 10 or N == 102:
        print(ret)
        return
    
    
    def check(N, broken: set, ret: int) -> int:
        """
        N에 도달할 수 있는 최소 횟수 구하기
        
        target: N을 인덱스화 시키기 위해 리스트로 변환
        length: N의 길이
        available: 누를 수 있는 숫자버튼들
        """
        target = list(map(int, list(str(N))))
        length = len(target)

        available = list(set(range(10)) - broken)
        idx = -1

        # 누를 수 없는 번호 중 가장 첫번째 번호의 인덱스 저장.
        # 모두 누를 수 있다면 번호의 길이를 바로 반환해줌.
        for i in range(length):
            if target[i] in broken:
                idx = i
                break
        else:
            return length  # N=102인경우 외에는 무조건 버튼을 직접 누르는게 유리함.
            # return min(ret, length)
        
        # 누를 수 없는 번호 직전까지의 숫자들
        head = target[:idx]

        # 누를 수 있는 번호들 중 최소, 최대값
        min_num = min(available)
        max_num = max(available)

        # 1. N보다 한자릿수 적은 길이의 번호
        # ex) N = 102, idx 노상관 => 99
        # 최대값이 0이거나 N이 한자릿수일 경우에는 건너뜀
        # 🚨 N이 한자리수일경우, length-1 = 0이므로, int("")가 되어버려 ValueError가 발생함.
        if max_num != 0 and length > 1:
            num = int(str(max_num) * (length-1))
            ret = min(ret, N - num + length - 1)
        
        # 2. idx = 0일경우, N보다 한자릿수 큰 길이의 번호
        # ex) N = 567, idx = 0 => 1000
        # 만약 누를 수 없는 번호가 0번째 인덱스라면, (0 제외)누를 수 있는 번호 중 최솟값을 앞자리에 붙여준다.
        if not head:
            head_num = [num for num in available if num != 0]
            if head_num:
                num = int(str(min(head_num)) + str(min_num) * length)
                ret = min(ret, num - N + length + 1)

        # 3. idx != 0일경우, 누를 수 없는 번호의 바로 앞번호를 변경
        # ex) N = 2345, idx = 1 => 1999 or 3000
        else:
            prev = head[-1]
            prev_head = "".join(map(str, head[:-1]))  # idx 전전까지만
            # 3.1 앞자릿수 바꿔주기
            upper = [num for num in available if num > prev]
            lower = [num for num in available if num < prev]

            # 큰 값 중 최솟값
            if upper:
                num = int(prev_head + str(min(upper)) + str(min_num)*(length - idx))
                ret = min(ret, len(str(num)) + (num - N))
            # 작은 값 중 최댓값
            if lower:
                num = int(prev_head + str(max(lower)) + str(max_num)*(length - idx))
                ret = min(ret, len(str(num)) + (N - num))

        # 4. 해당 자릿수부터 바꿔주기
        # ex) N = 2345, idx = 1 => 2299 or 2400
        upper = [num for num in available if num > target[idx]]
        lower = [num for num in available if num < target[idx]]

        head = "".join(map(str, head))
        if upper:
            num = int(head + str(min(upper)) + str(min_num)*(length - idx - 1))
            ret = min(ret, len(str(num)) + (num - N))
        if lower:
            num = int(head + str(max(lower)) + str(max_num)*(length - idx - 1))
            ret = min(ret, len(str(num)) + (N - num))

        return ret
    
    print(check(N, broken, ret))


main()