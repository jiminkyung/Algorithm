# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3915

# 조건을 제대로 확인해야하는 문제. 구현 연습하기 좋은듯. 나중에 또 풀어볼만한 문제다.
# 푸는데에 급급해서 코드가 더러움. 수정 필요함.
# 메모리: 33432KB / 시간: 216ms
from sys import stdin


def main():
    data = stdin.read().splitlines()[:-1]
    idx = 0

    while idx < len(data):
        # m: 책상 수, c: 책상당 최대 책 수, n: 학생 수
        m, c, n = map(int, data[idx].split())
        total_cost = 0
        idx += 1

        table = [[] for _ in range(m+1)]
        book_lst = []
        max_book_need = max(int(data[i]) for i in range(idx, idx + 2*n, 2))
        needed_books = [list(map(int, data[i].split())) for i in range(idx+1, idx + 2*n, 2)]
        asks = {}  # asks[x]: 책 x가 책상 D1에 놓여진 시간

        # for i in range(max_book_need):
        #     for j in range(idx+1, 2*n, 2):
        #         if len(data[j]) <= max_book_need:
        #             continue
        #         book_lst.append(data[j][i])

        for i in range(max_book_need):
            for j in range(n):
                if len(needed_books[j]) <= i:
                    continue
                book_lst.append(needed_books[j][i])
        
        for book in book_lst:
            if book not in table[-1]:
                table[-1].append(book)

        for book_lst_idx, book in enumerate(book_lst):
            # 책 찾기
            flag = False
            for table_num in range(m+1):
                if flag:
                    break

                curr_table = table[table_num]
                if curr_table:
                    for book_idx in range(len(curr_table)):
                        if curr_table[book_idx] == book:
                            new_table = curr_table[:book_idx] + curr_table[book_idx+1:]
                            table[table_num] = new_table
                            total_cost += table_num + 1
                            flag = True
                            break
            
            # 책 원위치
            if len(table[0]) < c:
                table[0].append(book)
                total_cost += 1
            else:
                # 임시 위치
                temp_table_num = m
                for table_num in range(1, m):
                    if len(table[table_num]) < c:
                        temp_table_num = table_num
                        table[table_num].append(book)
                        total_cost += table_num + 1
                        break
                else:
                    table[-1].append(book)
                    total_cost += m + 1
                
                oldest_book_idx = 0
                oldest_time = int(1e9)
                for i in range(c):
                    if oldest_time > asks[table[0][i]]:
                        oldest_book_idx = i
                        oldest_time = asks[table[0][i]]
                
                oldest_book = table[0][oldest_book_idx]
                table[0] = table[0][:oldest_book_idx] + table[0][oldest_book_idx+1:]
                total_cost += 1  # D1에서 오래된 책 빼기

                # 오래된 책 놓기
                for table_num in range(1, m):
                    if len(table[table_num]) < c:
                        table[table_num].append(oldest_book)
                        total_cost += table_num + 1
                        break
                else:
                    table[-1].append(oldest_book)
                    total_cost += m + 1
                
                # 임시 위치에서 꺼내기
                book_idx = table[temp_table_num].index(book)
                table[temp_table_num] = table[temp_table_num][:book_idx] + table[temp_table_num][book_idx+1:]
                total_cost += temp_table_num + 1

                # D1에 놓기
                table[0].append(book)
                total_cost += 1

            asks[book] = book_lst_idx
        
        print(total_cost)
        idx += 2*n


main()