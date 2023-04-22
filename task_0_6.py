def maximum(number_1, number_2, number_3):
    max_number = number_1
    if number_2 > max_number:
        max_number = number_2
    if number_3 > max_number:
        max_number = number_3
    return max_number


print(maximum(13, 8, 9))
