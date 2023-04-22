def find_common_letters(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    delimeter = ", "
    common_letters = []

    for letter in string_2:
        for character in string_1:
            if letter == character and letter not in common_letters:
                common_letters.append(letter)
    common_letters = delimeter.join(common_letters)
    print(f"Common letters: {common_letters}")


if __name__ == "__main__":
    find_common_letters("house", "computers")
