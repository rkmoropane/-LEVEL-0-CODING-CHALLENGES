def find_common_letters(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()

    set_1 = set(string_1)
    set_2 = set(string_2)

    common_letters = set_1 & set_2
    common_letters = sorted(list(common_letters))
    common_letters = [letter for letter in string_2 if letter in common_letters]

    common_letters = ", ".join(common_letters)
    print(f"Common letters: {common_letters}")


if __name__ == "__main__":
    find_common_letters("house", "computers")
