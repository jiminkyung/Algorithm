# 문자열


# 문제: https://www.acmicpc.net/problem/1148

# 🗝️단어별 문자 빈도수를 저장 -> 가장 많이 등장하는 단어(가운데), 적게 등장하는 단어(가운데 X)
# 단, 만족하는 단어가 없다면 퍼즐판의 문자들을 출력해야함.
# 관련 반례👉 https://www.acmicpc.net/board/view/78777


# 1) 단어 -> 퍼즐판 단계로 탐색
# Counter로 단어 딕셔너리를 한번씩만 생성하므로 효율적임
# 메모리: 48224KB / 시간: 740ms
from sys import stdin
from collections import Counter


def main():
    # 1. 입력 데이터 처리
    # "-"를 기준으로 나눈 후 첫번째 데이터는 단어들로, 두번째 데이터는 퍼즐판들로 저장
    data = stdin.read().split("-")

    words = data[0].splitlines()
    boards = data[1].splitlines()[1:-1]

    # 2. 퍼즐판 내의 문자 갯수 저장
    count = {}  # count[board]: board의 문자별 갯수
    ret = {}  # ret[board][a]: board의 문자 a로 만들 수 있는 단어들의 갯수
    for board in boards:
        count[board] = Counter(board)
        ret[board] = {}
    
    # 3. 단어별로 모든 퍼즐판 검사
    # 해당 퍼즐판으로 단어를 만들 수 있는지 체크, 가능하다면 ret 딕셔너리 업데이트
    for word in words:
        word_count = Counter(word)
        for board in boards:
            for alp in word_count:
                if count[board].get(alp, 0) < word_count[alp]:
                    break
            else:
                # ⭐문자 갯수를 그대로 더해주는게 X
                # 기준은 "만들수있는 단어 갯수"이기 때문에, 유형별로 한개씩만 체크한다.
                # ex) apple => a p l e 한개씩만 체크
                for alp in word_count:
                    ret[board][alp] = ret[board].get(alp, 0) + 1
    
    # 4. 퍼즐판별로 최대빈도, 최소빈도인 문자 탐색
    for board in boards:
        min_cnt, max_cnt = float("inf"), 0
        min_ret, max_ret = [], []

        for alp in set(board):
            ret_cnt = ret[board].get(alp, 0)

            if min_cnt > ret_cnt:
                min_cnt = ret_cnt
                min_ret = [alp]
            elif min_cnt == ret_cnt:
                min_ret.append(alp)
            
            if max_cnt < ret_cnt:
                max_cnt = ret_cnt
                max_ret = [alp]
            elif max_cnt == ret_cnt:
                max_ret.append(alp)
        
        min_ret = "".join(sorted(min_ret))
        max_ret = "".join(sorted(max_ret))

        print(min_ret, min_cnt, max_ret, max_cnt)


main()


# 2) 초기 풀이
# 퍼즐판 -> 단어 단계로 탐색함. 매번 단어용 딕셔너리(tmp)를 생성하므로 오래 걸림.
# 메모리: 48276KB / 시간: 3192ms
from sys import stdin
from collections import defaultdict


def main():
    data = stdin.read().split("-")

    words = data[0].splitlines()
    boards = data[1].splitlines()[1:-1]

    count = {}  # count[board][alp]: 문자 alp가 board내에 몇 개 존재하는지
    for board in boards:
        count[board] = defaultdict(int)
        for alp in board:
            count[board][alp] += 1
    
    def check(board: list, word: str) -> bool:
        """ 해당 퍼즐판으로 단어를 만들 수 있는지 체크 """
        tmp = defaultdict(int)

        for alp in word:
            tmp[alp] += 1
        
        for alp in tmp:
            if tmp[alp] > count[board][alp]:
                return False
        return True


    for board in boards:
        ret = defaultdict(int)  # ret[alp]: 문자 alp로 만들 수 있는 단어의 갯수
        for word in words:
            if check(board, word):
                for alp in set(word):
                    ret[alp] += 1
        
        min_cnt = float("inf")
        max_cnt = 0

        min_ret, max_ret = [], []

        for alp in set(board):
            if min_cnt > ret[alp]:
                min_cnt = ret[alp]
                min_ret = [alp]
            elif min_cnt == ret[alp]:
                min_ret.append(alp)
            
            if max_cnt < ret[alp]:
                max_cnt = ret[alp]
                max_ret = [alp]
            elif max_cnt == ret[alp]:
                max_ret.append(alp)
        
        min_ret = "".join(sorted(min_ret))
        max_ret = "".join(sorted(max_ret))
        
        print(min_ret, min_cnt, max_ret, max_cnt)


main()