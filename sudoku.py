import random

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    values_matrix = []
    for i in range (0 , len(values), n):
        values_matrix.append(values[slice(i,i+n)])
    return values_matrix

def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    for i in range(len(values)):
        if pos[0] == i:
            return values[i]

def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    column=[]
    for r in range(len(values)):
            column.append(values[r][pos[1]])
    return column


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    
    l = len(values)
    tmp = l/(pos[0]+1)
    if tmp>=3 and tmp<=9: row_ind = 0
    elif tmp<=2.25 and tmp>=1.5: row_ind = 3
    else: row_ind = 6
    
    tmp = l/(pos[1]+1)
    if tmp>=3 and tmp<=9: col_ind = 0
    elif tmp<=2.25 and tmp>=1.5: col_ind = 3
    else: col_ind = 6
    result=[]
    for r in range(row_ind,row_ind+3):
        for c in range(col_ind, col_ind+3):
            result.append(values[r][c])
    return result


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == '.':
                pos = row, col
                return pos
    return False


def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    row_values = get_row(grid,pos)
    block_values = get_block(grid,pos)
    col_values = get_col(grid,pos)
    possible_values = []
    for m in range(1,10):
        if not str(m) in row_values and not str(m) in col_values and not str(m) in block_values:
            possible_values.append(str(m))
    return possible_values

def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """
    m = True
    for row in range(0, 9):
        for col in range(0, 9):
            pos = row, col
            b = get_block(solution, pos)
            c = get_col(solution, pos)
            r = get_row(solution, pos)
            for i in range(1, 10):
                if not (str(i) in b and str(i) in c and str(i) in r):
                    m = False

    # Если решение solution верно, то вернуть True, в противном случае False
    return m

def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    pos = find_empty_positions(grid)
    if pos == False :
        return grid
    else:
        val = find_possible_values(grid, pos)
        for i in val:
            grid[pos[0]][pos[1]] = i
            if solve(grid):
                return grid
            else: grid[pos[0]][pos[1]] = '.'
    return False





grid = read_sudoku('C:\cs102\puzzle1.txt')
display(grid)
display(solve(grid))
print(check_solution(grid))

def replace(grid):
    posR = random.randint(0,8)
    posC = random.randint(0,8)
    pos = posR, posC
    s = find_possible_values(grid,pos)
    if grid[posR][posC] == '.' and s != []:
        grid[posR][posC] = s[0]
    else:
        grid = replace(grid)
    return grid

def f(grid):
    posR = random.randint(0,8)
    posC = random.randint(0,8)
    if grid[posR][posC] != '.':
        grid[posR][posC] = '.'
    else: 
        f(grid)
    return grid

def generate_sudoku(N):
    grid = []
    for i in range(81):
        grid.append('.')
    grid = group(grid, 9)
    d = random.randint(10,20)
    for i in range(0,d):
        grid = replace(grid)
    grid = solve(grid)
    for i in range(81-N):
        grid = f(grid)
    return grid

display(generate_sudoku(55))