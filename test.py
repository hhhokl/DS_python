def prime_nums(n):
    prime_numbers = list((2,))
    for outer_number in range(0, n):
        is_prime = False
        if outer_number > 1:
            for inner_number in range(min(prime_numbers), outer_number):
                if(outer_number % inner_number) == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True
        if is_prime:
            prime_numbers.append(outer_number)
    return prime_numbers

print(prime_nums(30))