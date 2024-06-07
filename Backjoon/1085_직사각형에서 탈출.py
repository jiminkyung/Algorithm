"""
제한사항:
1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
"""

x, y, w, h = map(int, input().split())

print(min(x, w-x, y, h-y))