def maximum(*numbers: int):
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number


print(maximum(1, 22, 3, 2))
