def find_vowels(string):
    vowels_found = []
    string = string.lower()
    vowels = "aeiou"
    for letter in string:
        if letter in vowels and letter not in vowels_found:
            vowels_found.append(letter)

    vowels_found_string = ", ".join(vowels_found)
    print(f"Vowels: {vowels_found_string}")


if __name__ == "__main__":
    find_vowels("Umuzi")
