"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.
"""

def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i] = pow(numbers[i], 2)
    return sum(numbers)

print(square_sum([1,2]))