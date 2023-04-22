def area_of_triangle(side_1, side_2, side_3):
    semi = 1 / 2 * (side_1 + side_2 + side_3)
    total_area = (semi * (semi - side_1) * (semi - side_2) * (semi - side_3)) ** (1 / 2)
    return total_area


if __name__ == "__main__":
    print(area_of_triangle(7, 6, 8))
