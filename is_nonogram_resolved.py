#!/usr/bin/env python3
specifications = (
        ((2,), (4,), (4,), (4,), (2,)),
        ((1, 1), (5,), (5,), (3,), (1,))
    )

solution = (
        (0, 1, 0, 1, 0),
        (1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1),
        (0, 1, 1, 1, 0),
        (0, 0, 1, 0, 0)
    )

def check_columns(specifications, solution):
    columns = specifications[0]
    rows = specifications[1]
    res_columns = ()
    for i in range(len(columns)):
        result = ()
        sum = 0
        if solution[-1][i] == 1:
            sum = 1
        for j in range(len(rows) - 1):
            if solution[j][i] == 1:
                sum += 1
                if solution[j+1][i] == 0:
                    result += (sum,)
                    sum = 0
        if sum != 0:
            result += (sum,)
        res_columns += ((result,))
    return res_columns

def check_rows(specifications, solution):
    columns = specifications[0]
    rows = specifications[1]
    res_rows = ()
    for i in range(len(rows)):
        result = ()
        sum = 0
        if solution[i][-1] == 1:
            sum = 1
        for j in range(len(columns) - 1):
            if solution[i][j] == 1:
                sum += 1
                if solution[i][j+1] == 0:
                    result += (sum,)
                    sum = 0
        if sum != 0:
            result += (sum,)
        res_rows += ((result,))
    return res_rows

def is_nonogram_resolved(specifications, solution):
    rows = specifications[1]
    print(rows)
    columns = specifications[0]
    print(columns)
    solution_rows = check_rows(rows, solution)
    solution_columns = check_columns(columns, solution)
    if solution_rows == rows and solution_columns == columns:
        return True
    return False

print(is_nonogram_resolved(specifications, solution))
