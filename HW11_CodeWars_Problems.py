#Problem 1: Sum of Multiples
#Description: Find the sum of all multiples of n below m

def sum_mul(n, m):
    numbers = []
    if n < 1 or m < 1:
            return 'INVALID'
    for i in range(n, m, n):
        numbers.append(i)
    return sum(numbers)

#Problem 2: Find the Remainder
#Description: Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
#Division by zero should return an empty value.

def remainder(a,b):
    if a == 0 and b == 0:
        return None
    if a > 0 and b == 0:
        return None
    elif b > 0 and a == 0:
        return None
    else:
        return max(a, b) % min(a, b)

#Problem 3: SpeedCode #2 - Array Madness
#Description: Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

def array_madness(a,b):
    squares = []
    cubes = []
    for i in a:
        squares.append(i**2)
    for j in b:
        cubes.append(j**3)
    if sum(squares) > sum(cubes):
        return True
    else:
        return False