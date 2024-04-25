def solution(todo_list, finished):
    return list(filter(lambda x: finished[todo_list.index(x)] == False, todo_list))