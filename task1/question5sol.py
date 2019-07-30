def min_in_list(numbers):
    minimum = numbers[0]
    for x in numbers:
        if x < minimum:
            minimum = x
    return minimum


nums = [1, 4, 7, -8, -11, 0, 4, 5, 6]
print(f'Minimum number in the list is : {min_in_list(nums)}')
