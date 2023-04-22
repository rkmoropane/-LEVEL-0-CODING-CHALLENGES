def celsius_to_fahrenheit(temperature):
    fahrenheit = temperature * (9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius


if __name__ == "__main__":
    print(celsius_to_fahrenheit(37))
    print(fahrenheit_to_celsius(98))
