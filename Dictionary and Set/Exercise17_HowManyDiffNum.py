def how_many_different_numbers(numbers):
    unique_number = set(numbers)
    return len(unique_number)

print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))