#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
        n (int): The number of rows of the triangle
    Returns:
        List of lists of integers representing the Pascal’s triangle
    '''
    if n <= 0:
        return []

    triange = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j-1])
        row.append(1)
        triangle.append(row)

    return triangle
