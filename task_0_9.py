def find_vowels(string):
    vowels_found = []
    delimeter = ", "
    string = string.lower()
    vowels = "aeiou"
    for letter in string:
        if letter in vowels:
            if letter not in vowels_found:
                vowels_found.append(letter)

    vowels_found = delimeter.join(vowels_found)
    print(f"Vowels: {vowels_found}")


if __name__ == "__main__":
    find_vowels("Umuzi")
