"""
Counter 함수를 사용한 풀이.
1. 각 크기별 갯수를 구해준다.
2. 갯수가 많은 순서대로 내림차순 정렬.
3. 정렬된 리스트를 순회하며, 갯수가 k개 이상이 되는 경우 i + 1 반환.(또는 start=1로 지정해준뒤 i 반환)
"""

from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)

    total = 0
    for i, count in enumerate(sorted_counts):
        total += count
        if total >= k:
            return i + 1

    return len(sorted_counts)