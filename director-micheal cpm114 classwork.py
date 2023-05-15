def find_largest_number(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest

# Example usage
numbers_list = [3, 8, 2, 10, 5]
largest_number = find_largest_number(numbers_list)
print("The largest number is:", largest_number)
