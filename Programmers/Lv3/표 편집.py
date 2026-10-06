# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/81303


# 구현 연습하기 좋은 문제
def solution(n: int, k: int, cmd: list[str]) -> str:
    # 연결 리스트처럼 이전노드, 다음노드를 저장
    # prev[x]: x의 이전노드 / nxt[x]: x의 다음노드
    # 원형으로 동작하는게 아니므로, 맨 앞/뒤 마지막 노드의 prev/nxt 값은 None으로 저장.
    prev = [i-1 for i in range(n)]
    nxt = [i+1 for i in range(n)]
    prev[0] = None
    nxt[n-1] = None

    curr = k
    delete = []  # 삭제된 행의 정보들. (행 번호, 이전노드, 다음노드)

    for i in range(len(cmd)):
        c, *num = cmd[i].split()

        if num:
            num = int(num[0])

        # 위/아래일 경우 num번동안 이전/다음노드를 타고 올라감
        if c == "U":
            for _ in range(num):
                curr = prev[curr]

        elif c == "D":
            for _ in range(num):
                curr = nxt[curr]
        
        # 삭제할 경우, (현재 노드(현재 행)의 번호, 이전노드, 다음노드)를 스택에 저장.
        elif c == "C":
            prev_idx = prev[curr]
            nxt_idx = nxt[curr]

            delete.append((curr, prev_idx, nxt_idx))

            # 이전노드가 존재할경우, 이전노드의 nxt에 삭제한 노드의 nxt를 저장
            # 🚨 if prev_idx 로 검사하게되면 prev_idx가 0인 경우를 걸러내지 못함!
            if prev_idx is not None:
                nxt[prev_idx] = nxt_idx
            # 다음노드가 존재할경우, 다음노드의 prev에 삭제한 노드의 prev를 저장
            if nxt_idx is not None:
                prev[nxt_idx] = prev_idx
            
            # 원래는 현재 행을 삭제하면 다음 행으로 포인터가 넘어감.
            # 하지만 삭제한 현재 행이 표의 마지막 행이었을 경우, 포인터를 이전 행으로 넘겨줘야함.
            if nxt_idx is not None:
                curr = nxt_idx
            else:
                curr = prev_idx
        # 복구시키는 경우
        else:
            # 가장 마지막에 삭제한 행의 정보를 스택에서 pop
            idx, prev_idx, nxt_idx = delete.pop()

            # 이전노드, 다음노드 정보를 원래와 같이 복원
            if prev_idx:
                nxt[prev_idx] = idx
            if nxt_idx:
                prev[nxt_idx] = idx
    
    # 삭제된 행은 X로 저장
    ret = ["O"] * n

    for idx, _, _ in delete:
        ret[idx] = "X"
    
    ret = "".join(ret)
    return ret