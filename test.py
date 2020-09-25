def sec_smallest(numbers):
    sec_smallest_number = numbers[0]
    for number in numbers:
        if number <= sec_smallest_number:
            sec_smallest_number = number
    return sec_smallest_number

num_list = [1, 2, -8, -8, -2, 0]
print(sec_smallest(num_list))