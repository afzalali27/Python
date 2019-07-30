def second_min(numbers):
    minimum = numbers[0]
    sec_min = minimum
    for x in numbers:
        if x < minimum:
            sec_min = minimum
            minimum = x
        elif x < sec_min:
            sec_min = x
    return sec_min


nums = [-2, 4, 7, -8, 11, 0, 4, 5, 6]
print(f'Second Minimum number in the list is : {second_min(nums)}')
input()
