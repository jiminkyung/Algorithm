"""
각 메뉴별로 어떤 번호에서 주문됐는지 딕셔너리에 담아주자~
했다가 뭔가... 이게 아닌것같았다.
찾아보니 백트래킹 문제였다.

두번째 코드는 클로드를 통해 얻어낸 풀이인데, combinations 모듈을 사용했다.
"""

# 뭔가 잘못됨을 느끼고 후퇴한 코드.
def solution(orders, course):
    cnt = {}
    for i, order in enumerate(orders):
        for menu in order:
            if menu not in cnt:
                cnt[menu] = [i]
            else:
                cnt[menu].append(i)
    return cnt

# 클로드 풀이.
from itertools import combinations

def solution(orders, course):
    cnt = {}  # 각 메뉴 조합의 주문 횟수를 저장하는 딕셔너리
    
    # 각 주문에 대해 메뉴 조합 생성
    for order in orders:
        # 2개부터 주문의 길이까지의 메뉴 개수에 대해 반복
        for i in range(2, len(order) + 1):
            # combinations 함수를 사용하여 i개의 메뉴로 구성된 조합 생성
            for combination in combinations(sorted(order), i):
                menu = ''.join(combination)  # 조합을 문자열로 변환
                
                # 메뉴 조합의 주문 횟수 카운트
                if menu not in cnt:
                    cnt[menu] = 1
                else:
                    cnt[menu] += 1
    
    result = []  # 가장 많이 주문된 메뉴 조합을 저장할 리스트
    
    # course에 지정된 메뉴 개수에 대해 반복
    for num in course:
        max_count = 0  # 현재까지 가장 많이 주문된 조합의 주문 횟수
        max_combinations = []  # 가장 많이 주문된 조합들을 저장할 리스트
        
        # cnt 딕셔너리의 각 메뉴 조합과 주문 횟수에 대해 반복
        for menu, count in cnt.items():
            # 현재 메뉴 조합의 길이가 num과 같은 경우에만 처리
            if len(menu) == num:
                # 현재 주문 횟수가 max_count보다 큰 경우
                if count > max_count:
                    max_count = count
                    max_combinations = [menu]
                # 현재 주문 횟수가 max_count와 같은 경우
                elif count == max_count:
                    max_combinations.append(menu)
        
        # 최소 2번 이상 주문된 메뉴 조합만 결과에 추가
        if max_count >= 2:
            result.extend(max_combinations)
    
    # 결과를 알파벳 순으로 정렬하여 반환
    return sorted(result)