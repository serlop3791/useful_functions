# Print concentric rectangular pattern in a 2d matrix.
#
# Let us show you some examples to clarify what we mean.
#
# Example 1:
#
# Input: A = 4.
#
# Output:
#
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4


# Example 2:
#
# Input: A = 3.
#
# Output:
#
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
# The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.
#
# You will be given A as an argument to the function you need to implement, and you need to return a 2D array.


# # Example 2:
# #
# # Input: A = 3.
# #
# # Output:
# #
# # 3 3 3 3 3
# # 3 2 2 2 3
# # 3 2 1 2 3
# # 3 2 2 2 3
# # 3 3 3 3 3


def get_empty_matrix(size):
    rows_count, cols_count = size, size
    return [[0 for _ in range(cols_count)] for _ in range(rows_count)]


def print_matrix_rows(matrix):
    for i in range(len(matrix)):
        print(str(matrix[i]), end='\n')


# print_matrix_rows(get_empty_matrix(5))

def fill_matrix(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = count
            count += 1
    return matrix


# print_matrix_rows(fill_matrix(get_empty_matrix(3)))

# matrix = get_empty_matrix(2)


# # Input: A = 2.
# # Output:
# # 2 2 2
# # 2 1 2
# # 2 2 2

matrix = fill_matrix(get_empty_matrix(3))
print_matrix_rows(matrix)


# end of top right
# end of bottom right
# end of bottom left
# end of top left
# concentric traversal
# 0 1 2 5 8 7 6 3 4
#
# for i in range(0, len(matrix[0])):
#     print(matrix[0][i], end=' ')
# print(" ")
# for i in range(0, len(matrix)):
#     # i = 1, j = 2 or j = len(matrix[i]) - 1
#     num_to_print = matrix[0]
#     # print(i, end=' ')


# Python3 program for printing
# the rectangular pattern

# Function to print the pattern
def printPattern(n):
    # a = n, b = n – 1, c = n – 2
    # number of rows and columns to be printed
    s = 2 * n - 1

    # Upper Half
    for i in range(0, int(s / 2) + 1):

        m = n

        # Decreasing part
        for j in range(0, i):
            print(m, end=" ")
            m -= 1

        # Constant Part
        for k in range(0, s - 2 * i):
            print(n - i, end=" ")

        # Increasing part.
        m = n - i + 1
        for l in range(0, i):
            print(m, end=" ")
            m += 1

        print("")

    # Lower Half
    for i in range(int(s / 2), -1, -1):

        # Decreasing Part
        m = n
        for j in range(0, i):
            print(m, end=" ")
            m -= 1

        # Constant Part.
        for k in range(0, s - 2 * i):
            print(n - i, end=" ")

        # Decreasing Part
        m = n - i + 1
        for l in range(0, i):
            print(m, end=" ")
            m += 1

        print("")


# Driven Program
if __name__ == '__main__':
    n = 3
    printPattern(n)

# this code is contributed by Smitha Dinesh
# Semwal


# Python3 program for printing
# the rectangular pattern

# Function to print the pattern
# def printPattern(n):
#     arraySize = n * 2 - 1;
#     result = [[0 for x in range(arraySize)]
#               for y in range(arraySize)];
#
#     # Fill the values
#     for i in range(arraySize):
#         for j in range(arraySize):
#             if (abs(i - (arraySize // 2)) >
#                     abs(j - (arraySize // 2))):
#                 result[i][j] = abs(i - (arraySize // 2)) + 1;
#             else:
#                 result[i][j] = abs(j - (arraySize // 2)) + 1;
#
#     # Print the array
#     for i in range(arraySize):
#         for j in range(arraySize):
#             print(result[i][j], end=" ");
#         print("");
#
#
# # Driver Code
# n = 3;
#
# printPattern(n);

# This code is contributed by mits


