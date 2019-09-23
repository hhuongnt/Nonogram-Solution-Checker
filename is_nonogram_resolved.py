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
    result = ()
    for i in range(len(specifications[0])):
        sum = 0
        for j in range(len(specifications[0])):
            if solution[j][i] == 1:
                sum += 1
        result += ((sum,),)
        print(sum)
    return result

def check_rows(specifications, solution):
    result = ()
    res = ()
    for i in range(len(specifications[1])):
        sum = 0
        for j in range(len(specifications[1]) - 1):
            if solution[i][j] == 1:
                sum += 1
                if solution[i][j+1] == 0:
                    result += (sum,)
                    sum = 0
                else:
                    sum += 1
            print(result)
        # res += ((result,))
        result = ()
    return res

def is_nonogram_resolved(specifications, solution):
    pass

print(check_columns(specifications, solution))
print(check_rows(specifications, solution))
