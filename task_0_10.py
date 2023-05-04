def find_common_letters(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()

    common_letters = [letter for letter in string_2 if letter in string_1]

    common_letters = ", ".join(common_letters)
    print(f"Common letters: {common_letters}")


if __name__ == "__main__":
    find_common_letters("house", "computers")
