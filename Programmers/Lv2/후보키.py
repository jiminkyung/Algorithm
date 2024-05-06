"""
1. 유일성
2. 최소성
을 만족하는 후보키를 찾아내는 문제.
아래는 AI를 통해 얻은 풀이다.
itertools의 combinations(조합) 모듈을 사용해도 되지만,
비트마스크를 사용하여 더 효율적인 풀이를 얻어냈다.

🌟 추가로, 모든 조합의 경우는 2^(요소의 갯수) 로 알아낼 수 있다.
다만 공집합이 추가된 경우이기 때문에 -1을 해줘야하므로 1부터 15까지만 순회한다.
"""

def solution(relation):
    """
    relation: 릴레이션(2차원 리스트)
    
    후보 키의 개수를 반환하는 함수
    """
    num_attributes = len(relation[0])  # 속성의 개수
    candidate_keys = []  # 후보 키를 저장할 리스트

    def is_unique(relation, subset):
        """
        relation: 릴레이션(2차원 리스트)
        subset: 속성 조합(비트마스크)
        
        속성 조합이 유일성을 만족하는지 검사하는 함수
        """
        selected_tuples = []
        for row in relation:
            current_tuple = tuple(row[i] for i in range(len(row)) if subset & (1 << i))
            if current_tuple in selected_tuples:
                return False
            selected_tuples.append(current_tuple)
        return True

    def is_minimal(candidate_keys, subset):
        """
        candidate_keys: 후보 키 리스트
        subset: 속성 조합(비트마스크)
        
        속성 조합이 최소성을 만족하는지 검사하는 함수
        """
        for key in candidate_keys:
            if (key & subset) == key:
                return False
        return True

    # 모든 가능한 속성 조합에 대해 유일성과 최소성 검사
    for i in range(1, 1 << num_attributes):
        if is_unique(relation, i) and is_minimal(candidate_keys, i):
            candidate_keys.append(i)

    return len(candidate_keys)