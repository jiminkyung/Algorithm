# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/160585


# 조건 문제
def solution(board: list[str]) -> int:

    def check(val: str) -> bool:
        """ 우승 확인 함수 """

        # 오른쪽, 아래, 대각선만 체크
        flag = all(board[i][i] == val for i in range(3)) or all(board[i][2-i] == val for i in range(3))

        for i in range(3):
            if all(board[i][j] == val for j in range(3)):
                flag = True
                break
        
        for j in range(3):
            if all(board[i][j] == val for i in range(3)):
                flag = True
                break
        
        return flag


    x_flag = check("X")
    o_flag = check("O")

    x_cnt = sum(line.count("X") for line in board)
    o_cnt = sum(line.count("O") for line in board)

    # 처음엔 조건을 복잡하게 설정했었는데, 질문글을 보고 수정함.

    # X와 O갯수가 같은 경우 -> (아무 수도 두지 않았을경우) or (아직 두고있고 O가 이기지 않았을경우) 성립.
    if x_cnt == o_cnt and not o_flag:
        return 1
    
    # X와 O갯수가 1 차이나는 경우 -> X 선공 규칙을 준수하는중임. -> X가 이기지 않았을경우 성립.
    if o_cnt - x_cnt == 1 and not x_flag:
        return 1
    
    return 0