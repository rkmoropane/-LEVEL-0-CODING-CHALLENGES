def convert_minutes_to_hours_and_minutes(number):
    hours = number // 60
    min = number % 60
    hour_string = "hours" if hours != 1 else "hour"
    minutes_string = "minutes" if min != 1 else "minute"

    result = f"{hours} {hour_string}, {min} {minutes_string}"
    return result


print(convert_minutes_to_hours_and_minutes(61))
print(convert_minutes_to_hours_and_minutes(121))
print(convert_minutes_to_hours_and_minutes(31))
