"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
"""

def sum_two_smallest_numbers(numbers):
    min1 = numbers[0]
    min2 = numbers[1]
    for i in range(len(numbers)):
        if numbers[i] < min1:
            min1 = numbers[i]
    for i in range(len(numbers)):
        if numbers[i] < min2 and numbers[i]!= min1:
            min2 = numbers[i]
    return min1+min2

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))