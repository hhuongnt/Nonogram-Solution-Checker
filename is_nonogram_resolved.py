#!/usr/bin/env python3

# check solution columns
def check_columns(specifications, solution):
    """
    Count the value 1 of each column in proposed solution and return a tuple of
    result for each column. Return tuple contain all solution column results.


    @specifications: the specifications of a nonogram.

    @solution: a proposed solution.

    @return: a tuple contain all column results.
    """

    # solution columns
    columns = len(solution[0])

    # solution rows
    rows = len(solution)

    # final columns result variable
    res_columns = ()

    # loop though solution columns.
    for i in range(columns):

        # temp variable to contain result of each colum25x35ns
        result = ()

        # init sum
        sum = 0

        # loop though solution rows, except last value to check later
        for j in range(rows - 1):

            # check if value = 1
            if solution[j][i] == 1:

                # add sum by 1
                sum += 1

                # if the after value = 0
                if solution[j+1][i] == 0:

                    # add sum to result
                    result += (sum,)

                    # reset sum
                    sum = 0

        # check last value. If it = 1, add sum by 1 else do nothing
        if solution[-1][i] == 1:
            sum += 1

        # end of loop check if sum > 0, add sum to result
        if sum != 0:
            result += (sum,)

        # add current column result to final columns result
        res_columns += ((result,))

    # return final columns result
    return res_columns


# check solution rows
def check_rows(specifications, solution):
    """
    Count the value 1 of each row in proposed solution and return a tuple of
    result for each row. Return tuple contain all solution row results.


    @specifications: the specifications of a nonogram.

    @solution: a proposed solution.

    @return: a tuple contain all row results.
    """

    # solution column
    columns = len(solution[0])

    # solution rows
    rows = len(solution)

    # final rows result variable
    res_rows = ()

    # loop though solution rows
    for i in range(rows):

        # temp variable to contain result of each rows
        result = ()

        #init sum
        sum = 0

        # loop though solution columns, except last value to check later
        for j in range(columns - 1):

            # check if value = 1
            if solution[i][j] == 1:

                # add sum by 1
                sum += 1

                # if the after value = 0
                if solution[i][j+1] == 0:

                    # add sum to result
                    result += (sum,)

                    # reset sum
                    sum = 0

        # check last value. If it = 1, add sum by 1 else do nothing
        if solution[i][-1] == 1:
            sum += 1

        # end of loop check if sum > 0, add sum to result
        if sum != 0:
            result += (sum,)

        # add current row result to final rows result
        res_rows += ((result,))

    # return final rows result
    return res_rows

def catch_specifications_error(specifications):
    """
    Catch error in specifications' format.
    """

    # specifications' format isn't tuple
    if type(specifications) != tuple:
        raise TypeError("Specifications' format isn't tuple")

    # Specifications is missing row/col
    if len(specifications) < 2:
        raise ValueError("Specifications is missing row/col")
    elif len(specifications) > 2:
        raise ValueError("Specifications is more row/col")

    # loop though specifications to catch error
    for tups in specifications:
        for tup in tups:

            # Missing commas after number
            if type(tup) != tuple:
                raise TypeError("Missing commas after number")
            for value in tup:

                # Too much level of tuple in tuple element
                if type(value) != int:
                    raise TypeError("Too much level of tuple in tuple element")

    # check nonogram exist
    rows = specifications[0]
    for tup in rows:
        sum = 0
        for value in tup:
            sum += value
        if sum > len(specifications[1]):
            raise ValueError("Nonogram cannot exist")


def is_nonogram_resolved(specifications, solution):
    """
    Returns True if the suggested solution successfully matches
    the nonogram's specifications, False otherwise.


    @specifications: the specifications of a nonogram.

    @solution: a proposed solution.

    @return: True if solution = specifications, else False.
    """
    catch_specifications_error(specifications)

    # get specifications rows
    rows = specifications[1]

    # get specifications columns
    columns = specifications[0]

    # get solution rows
    solution_rows = check_rows(specifications, solution)

    # get solution columns
    solution_columns = check_columns(specifications, solution)

    # check if solution row = specifications row and check columns
    if solution_rows == rows and solution_columns == columns:

        # return True if solution = specifications
        return True

    # else return False
    return False


if __name__ == '__main__':
    # # Specifications 25x35
    # specifications = ( ((4,),(2,4,),(2,2, 2, 1,),(3, 2, 5,),(2, 1, 1, 5,),(1, 2, 2, 1, 5,),(1, 2, 1, 2, 1, 5, 1,),(1, 3, 1, 3, 3, 1, 1,),(1, 4, 1, 3, 3, 1, 5,),(2, 2, 1, 5, 1, 9,),(1, 1, 1, 1, 1, 15,),(1, 1, 1, 2, 2, 2, 10, 2,),(1, 2, 2, 1, 1, 1, 7, 1, 2,),(1, 1, 1, 1, 2, 6, 2, 2,),(1, 2, 1, 1, 2, 5, 1, 3,),(1, 2, 1, 4, 4, 2, 3,),(1, 2, 2, 1, 3, 3, 3, 1, 2,),(1, 3, 1, 6, 5, 1, 2,),(4, 1, 1, 2, 2, 2, 2, 2, 1,),(1, 2, 2, 1, 2, 1, 2, 2, 3,),(1, 2, 1, 2, 1, 2, 2, 1,),(1, 2, 5, 1, 2, 1,),(2, 4, 4,),(5, 1, 3,),(2,)),
    # ((4,),(2, 1,),(1, 4, 2,),(3, 2, 3, 1, 3,),(2, 1, 2, 3, 2,),(1, 1, 1, 6, 1, 1,),(2, 2, 2, 2, 2, 1,),(1, 3, 3, 2, 1,),(2, 6, 5, 2,),(1, 2, 5, 2,),(3, 3, 5,),(1, 2, 2, 2,),(8, 1, 1,),(1, 2, 2,),         (1, 4,),         (4, 3,),         (5, 4,),         (4, 9,),(1, 2, 6, 1, 1,),(7, 1,),(5, 5, 3,),(8, 4, 7,),(1, 11, 5, 2,),(1, 7, 3, 3, 2,),(7, 12,),(2, 4, 4,),(2, 3,),(2, 4,),(5,),(2, 5,),(3, 4, 2, 1,),(10,2,),(4,4,),(4,),(2,))
    # )
    #
    # # True
    # solution = ( (0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,0,0,0, 0,0,0,0,0),
    # (0,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,1,0,0, 0,0,0,0,0), (0,0,0,0,0, 0,0,0,0,0, 1,0,0,1,1, 1,1,0,1,1, 0,0,0,0,0), (0,0,0,0,0, 0,0,1,1,1, 0,1,1,0,1, 1,1,0,1,0, 1,1,1,0,0), (0,0,0,0,0, 1,1,0,0,1, 0,0,1,1,0, 0,0,1,1,1, 0,0,1,1,0), (0,0,0,0,1, 0,0,0,1,0, 1,0,0,0,1, 1,1,1,1,1, 0,1,0,1,0),
    # (0,0,0,1,1, 0,0,1,1,0, 0,1,1,0,0, 0,1,1,0,0, 1,1,0,1,0), (0,0,0,1,0, 0,0,1,1,1, 0,0,1,1,1, 0,0,0,0,1, 1,0,0,1,0), (0,0,1,1,0, 0,1,1,1,1, 1,1,0,0,0, 1,1,1,1,1, 0,0,1,1,0), (0,0,1,0,0, 1,1,0,0,0, 0,1,1,1,1, 1,0,0,0,0, 0,1,1,0,0), (0,0,0,1,1, 1,0,0,0,0, 0,0,0,1,1, 1,0,0,1,1, 1,1,1,0,0),
    # (0,0,0,1,0, 0,0,0,0,0, 0,1,1,0,0, 1,1,0,0,0, 0,1,1,0,0), (0,0,0,0,1, 1,1,1,1,1, 1,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0), (0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 1,1,0,0,0), (0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 1,0,0,0,0), (0,0,0,0,0, 0,1,1,1,1, 0,0,0,0,0, 0,0,1,1,1, 0,0,0,0,0),
    # (0,0,0,0,0, 0,0,1,1,1, 1,1,0,0,1, 1,1,1,0,0, 0,0,0,0,0), (0,0,0,0,0, 0,1,1,1,1, 0,1,1,1,1, 1,1,1,1,1, 0,0,0,0,0), (0,0,0,0,0, 1,0,0,0,1, 1,0,0,1,1, 1,1,1,1,0, 1,0,0,1,0), (0,0,0,0,0, 0,0,0,0,1, 1,1,1,1,1, 1,0,0,0,0, 0,0,0,0,1), (0,0,1,1,1, 1,1,0,0,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,1,1,1),
    # (0,1,1,1,1, 1,1,1,1,0, 1,1,1,1,0, 0,0,1,1,1, 1,1,1,1,0), (0,1,0,1,1, 1,1,1,1,1, 1,1,1,1,0, 0,1,1,1,1, 1,0,1,1,0), (1,0,1,1,1, 1,1,1,1,0, 1,1,1,0,0, 1,1,1,0,0, 0,1,1,0,0), (1,1,1,1,1, 1,1,0,0,0, 1,1,1,1,1, 1,1,1,1,1, 1,1,0,0,0), (1,1,0,0,0, 0,0,0,0,0, 1,1,1,1,0, 0,0,1,1,1, 1,0,0,0,0),
    # (1,1,0,0,0, 0,0,0,0,1, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0), (0,1,1,0,0, 0,0,0,0,1, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0), (0,0,0,0,0, 0,0,1,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0), (0,0,0,0,0, 0,0,0,0,1, 1,0,0,0,1, 1,1,1,1,0, 0,0,0,0,0), (0,0,0,0,0, 0,0,0,1,1, 1,0,1,1,1, 1,0,0,1,1, 0,1,0,0,0),
    # (0,0,0,0,0, 0,0,0,1,1, 1,1,1,1,1, 1,1,1,0,1, 1,0,0,0,0), (0,0,0,0,0, 0,0,0,1,1, 1,1,0,0,0, 0,1,1,1,1, 0,0,0,0,0), (0,0,0,0,0, 0,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0), (0,0,0,0,0, 0,0,0,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0)
    # )

    # # Missing commas after number '2'
    # specifications = (
    #     ((2), (3, 6)),
    #     ((1,), (3, 5))
    # )

    # # Too much level of tuple in tuple element
    # specifications = (
    #     (((2, ), ), (3, 6)),
    #     ((1,), (3, 5))
    # )

    # # Nonogram cannot exist
    # specifications = (
    #     ((2,), (6,)),
    #     ((1,), (2,))
    # )

    # # Specifications' format isn't tuple
    # specifications = [
    #     ((2,), (1,)),
    #     ((1,), (2,))
    # ]

    # # Specifications is missing row/col
    # specifications = (
    #     ((2,), (6,)),
    # )

    # # Specifications is more row/col
    # specifications = (
    #     ((2,), (6,)),
    #     ((1,), (2,)),
    #     ((1,), (2,))
    # )

    # # Specifications 1x1
    # specifications = (
    #     ((1,),),print(is_nonogram_resolved(specifications_15x15, solution_15x15_true))
    #     ((1,),)
    # )
    # solution = (
    #     (1,),
    # )

    # # multi elements column, row
    # specifications_5x5 = (
    #     ((2,), (4,), (4,), (4,), (2,)),
    #     ((1, 1), (5,), (5,), (3,), (1,))
    # )
    # solution_5x5_false = (
    #     (0, 1, 0, 0, 0),
    #     (1, 1, 1, 1, 1),
    #     (1, 1, 1, 1, 1),
    #     (0, 1, 1, 1, 0),
    #     (0, 0, 1, 0, 0)
    # )
    # solution_5x5_true = (
    #     (0, 1, 0, 1, 0),
    #     (1, 1, 1, 1, 1),
    #     (1, 1, 1, 1, 1),
    #     (0, 1, 1, 1, 0),
    #     (0, 0, 1, 0, 0)
    # )
    # print(is_nonogram_resolved(specifications_5x5, solution_5x5_false))
    # print(is_nonogram_resolved(specifications_5x5, solution_5x5_true))

    # Nonogram 15x15
    specifications_15x15 = (
        ((2, 4, 2, 1), (3, 2, 1, 1, 1), (1, 2, 1, 1, 2, 1), (1, 1, 1, 1, 5),
         (1, 1, 1, 2, 3), (1, 8, 3), (6, 3, 2), (5, 1, 2), (1, 1, 2, 1, 1),
         (3, 2, 1, 3), (1, 1, 1, 2), (1, 1, 2, 4, 1), (1, 2, 1, 1, 2),
         (1, 4, 2, 3), (9, 1, 2)),
        ((3, 1, 1, 1, 1), (2, 1, 4, 2), (4, 2, 4, 1), (1, 6, 1), (1, 3, 4),
         (7, 1, 5), (1, 5, 2), (1, 2, 1, 1, 4), (2, 3, 1, 2, 1), (4, 1, 3),
         (1, 2, 1, 2), (1, 2, 2), (8, 2, 3), (5, 6), (3, 2, 1))
    )
    solution_15x15_true = (
        (0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1),
        (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1),
        (0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1),
        (1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1),
        (1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1),
        (0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0),
        (0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1),
        (1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1),
        (0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0),
        )
    print(is_nonogram_resolved(specifications_15x15, solution_15x15_true))

    # print(is_nonogram_resolved(specifications, solution))
