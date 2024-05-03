"""
알고리즘 수업때 풀어봤던 문제.
"""

def solution(record: list) -> list:
    users = {}
    answers = []
    for r in record:
        state, user, *nickname = r.split()
        if state == "Enter":
            users[user] = nickname[0]
            answers.append([user, "님이 들어왔습니다."])
        elif state == "Leave":
            answers.append([user, "님이 나갔습니다."])
        else:
            users[user] = nickname[0]
    return [users[user] + state for user, state in answers]

# 정답 코드 중 발견한 두줄코드. 가독성이 너무 떨어진다.
def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]

# 가장 좋아요가 많았던 코드. 나도 state를 딕셔너리로 만들까 고민했었는데 마침 적절한 풀이가 있었다.
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer