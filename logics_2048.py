import random
import copy
#from main import mas

""" mas  = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ] """

def pretty_print(lst):
    print('-'*10)
    for row in lst:
        print(*row)
    print('-'*10)

def get_number_from_index(i, j):
    return i * 4 + j + 1

def get_index_from_number(lst):
    lst -= 1
    i, j = lst//4, lst % 4
    return i, j

def insert_2_or_4(lst, i, j):
    if random.random() <= 0.75:
        lst[i][j] = 2
    else:
        lst[i][j] = 4
    return lst

def get_empty_list(lst):
    empty = []
    for i in range(4):
        for j in range(4):
            if lst[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

def is_zero_in_mas(lst):
    for row in lst:
        if 0 in row:
            return True
    return False

def move_left(lst):
    origin = copy.deepcopy(lst)
    delta = 0
    for row in lst:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if lst[i][j] == lst[i][j + 1] and lst[i][j] != 0:
                lst[i][j] *= 2
                delta += lst[i][j]
                lst[i].pop(j + 1)
                lst[i].append(0)
    return lst, delta, not origin == lst

def move_right(lst):
    origin = copy.deepcopy(lst)
    delta = 0
    for row in lst:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3, 0, -1):
            if lst[i][j] == lst[i][j - 1] and lst[i][j] != 0:                               
                lst[i][j] *= 2
                delta += lst[i][j]                
                lst[i].pop(j - 1)
                lst[i].insert(0,0)
    return lst, delta, not origin == lst

def move_up(lst):
    origin = copy.deepcopy(lst)
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if lst[i][j] != 0:
                column.append(lst[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i + 1] and column[i] != 0:                
                column[i] *= 2
                delta += column[i]
                column.pop(i + 1)
                column.append(0)
        for i in range(4):
            lst[i][j] = column[i]        
    return lst, delta, not origin == lst

def move_down(lst):
    origin = copy.deepcopy(lst)
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if lst[i][j] != 0:
                column.append(lst[i][j])
        while len(column) != 4:
            column.insert(0,0)
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:                
                column[i] *= 2
                delta += column[i]
                column.pop(i - 1)
                column.insert(0,0)
        for i in range(4):
            lst[i][j] = column[i]
    return lst, delta, not origin == lst

def can_move(lst):
    for i in range(3):
        for j in range(3):
            if lst[i][j] == lst[i][j + 1] or lst[i][j] == lst[i + 1][j]:
                return True
    for i in range(1,4):
        for j in range(1,4):
            if lst[i][j] == lst[i - 1][j] or lst[i][j] == lst[i][j - 1]:
                return True
    return False
