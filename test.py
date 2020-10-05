def recursive_list_sum(data_list):
    total_sum = 0
    for list_part in data_list:
        if(type(list_part) is type(list())):
            total_sum += recursive_list_sum(list_part)
        else:
            total_sum += list_part
    return total_sum



print('The sum of a list is ', recursive_list_sum([1, 2, [3, 4], [5, 6], [7, 8, 9, [10]]]))