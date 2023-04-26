def convert_minutes_to_hours_and_minutes(number):
    hours = number // 60
    min = number % 60
    hour_string = "hours" if hours != 1 else "hour"
    minutes_string = "minutes" if min != 1 else "minute"

    result = f"{hours} {hour_string}, {min} {minutes_string}"
    print(result)


if __name__ == "__main__":
    convert_minutes_to_hours_and_minutes(71)
    convert_minutes_to_hours_and_minutes(133)
    convert_minutes_to_hours_and_minutes(30)
