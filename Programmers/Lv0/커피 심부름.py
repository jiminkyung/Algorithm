def solution(order):
    count = 0
    for menu in order:
        if "americano" in menu or "anything" in menu:
            count += 4500
        else:
            count += 5000
    return count