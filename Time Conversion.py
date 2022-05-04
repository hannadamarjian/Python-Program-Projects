def add_time(start, duration, day):
    global extra_hour, min_dur, value, add_numb_of_days

    def fixing_hours(a, b):
        hour_sum = a + b
        if hour_sum % 12 == 0:
            hour_str = str(12)  # USE AS PART OF FINAL OUTPUT

        else:
            hour_str = str(hour_sum % 12)  # USE AS PART OF FINAL OUTPUT

        return hour_str

    def exact_minute(c):
        min_str = c * 2
        return min_str

    def singular_digits(d):
        min_str = '0' + str(d)
        return min_str

    # Goal 1: focus on the HOUR implementation:

    # a.) For start time (first argument):
    hour_and_min1 = start.split(
        ':')  # create a list where the first element is the hour, the second is the minute, and the third (optional) is AM or PM.
    start_hour = int(hour_and_min1[0])  # Retrieve hour and convert it to an integer.

    # b.) For duration time (second argument):
    hour_and_min2 = duration.split(':')
    dur_hour = int(hour_and_min2[0])

    # c.) Take the sum of the two numbers. We want to divide by 12 (since that is the MAXIMUM hour value) and save the remainder. Thus, we use a modulus (% in Python language) b.
    hour_str = fixing_hours(start_hour, dur_hour)

    # ------------------------------------------------ (we are still in the function) -----------------------------------

    # Goal 2: focus on the MINUTE implementation:

    # a.) For start time (first argument):
    min_and_am_or_pm = hour_and_min1[1].split(' ')  # Note this includes the meridiem and the minute!
    start_min = int(min_and_am_or_pm[0])
    orig_meridiem = min_and_am_or_pm[1]


    min_and_am_or_pm2 = hour_and_min2[1].split(' ')  # Note this does NOT include the meridiem but ONLY the minute!
    dur_min = int(min_and_am_or_pm2[0])

    # b.) Take the sum of the two numbers. We want to divide by 60 (since that is the MAXIMUM minute value) and save the remainder. Thus, we use a modulus (% in Python language) b.
    min_sum = start_min + dur_min
    if min_sum > 59:  # min > 60
        min_dur = (start_min + dur_min) % 60  # integer is between 1-59, inclusive.
        min_str = str(min_dur)  # convert to string for output.

        if min_str == '0':  # for numbers like 60, 120, 180, etc. (multiples of 60)
            min_str = exact_minute(min_str)  # '00' for final minute output.


        elif 1 <= min_dur <= 9:
            min_str = singular_digits(min_dur)


        else:
            min_str = min_str

        extra_hour = int(min_sum / 60)  # save any extra hours in memory.

        if start_hour + dur_hour + extra_hour > 12:  # 11 + 2 + 1 (see Example 2 on freeCodeCamp.org)
            extra_hour2 = dur_hour + extra_hour
            hour_str = fixing_hours(start_hour,
                                    extra_hour2)  # additional duration --> function call if an example like this happens: 12 + 1 or 13 + 42 or 2 + 14.

        else:
            hour_dur = start_hour + dur_hour + extra_hour  # 3 + 2 + 1 = 6
            hour_str = str(hour_dur)

    else:  # min < 60
        min_str = str(min_sum)  # USE AS PART OF FINAL OUTPUT
        if min_str == '0':
            min_str = exact_minute(min_str)  # '00' for final minute output.


        elif 1 <= min_sum <= 9:
            min_str = singular_digits(min_sum)


        else:
            min_str = min_str

    # ------------------------------------------------ (we are still in the function) -----------------------------------

    # Goal 3: focus on the MERIDIEM implementation:

    extra_hour = int(min_sum / 60)  # save any extra hours in memory.
    i = 0  # used for time ranges to determine meridiem.
    total_dur_hours = dur_hour + extra_hour
    while i <= total_dur_hours:
        if (11 - start_hour < total_dur_hours and i == 0) or (start_min + dur_min >= 60 and i == 0):
            if min_and_am_or_pm[1] == 'AM' and total_dur_hours >= 12 - start_hour:  # convert from AM to PM
                min_and_am_or_pm[1] = "PM"  # lists are mutable, so it is okay to change an element in the list "min_and_am_or_pm"
            else:
                min_and_am_or_pm[1] = 'AM'  # keep the same meridiem value
            i += 1
        if 12 * (i + 1) - start_hour <= total_dur_hours <= 12 * (i + 2) - start_hour:
            if min_and_am_or_pm[1] == 'AM':
                min_and_am_or_pm[1] = "PM"
                i += 1
            else:
                min_and_am_or_pm[1] = "AM"
                i += 1
        else:
            break

    meridiem = min_and_am_or_pm[1]

    # ------------------------------------------------ (we are still in the function) -----------------------------------

    # Goal 4: focus on the WEEKDAY implementation:

    # First, convert the weekday into all caps and then assign it to its correct syntax:

    weekday = day.lower()  # make the day all lowercase (it is a string) and assign it to a variable called "weekday".
    first_char = weekday[0].upper()
    weekday = first_char + weekday[1:]

    days = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}

    counter = 0
    value = ''
    for day in days.keys():
        counter += 1
        if weekday == day:
            value = days[weekday]
            break
        else:
            if counter > 7:
                break
            else:
                continue

    # Handle adding one day to the clock counter before adding every 24 hours increments:
    add_numb_of_days = 0

    if orig_meridiem == 'AM':
        if total_dur_hours > 24 - start_hour:
            total_dur_hours = total_dur_hours - (24 - start_hour)
            add_numb_of_days += 1
            if total_dur_hours >= 24:
                extra_days = int(total_dur_hours / 24)
                add_numb_of_days += extra_days
    else:
        if total_dur_hours > 24 - start_hour - 12:
            total_dur_hours = total_dur_hours - (24 - start_hour - 12)
            add_numb_of_days += 1
            if total_dur_hours >= 24:
                extra_days = int(total_dur_hours / 24)
                add_numb_of_days += extra_days


    if value != '' and value + add_numb_of_days > max(days.values()):  # greater than "max(days.values()) = 6"
        day_in_future_value = ((value + add_numb_of_days) % 7) + 1
        if day_in_future_value == 7:
            day_in_future = 'Sunday'
        else:
            day_list = list(days.keys())
            value_list = list(days.values())
            position = value_list.index(day_in_future_value)
            day_in_future = day_list[position]
    elif value != '' and value + add_numb_of_days <= max(days.values()):
        day_in_future_value = (value + add_numb_of_days) % 7
        day_list = list(days.keys())
        value_list = list(days.values())
        position = value_list.index(day_in_future_value)
        day_in_future = day_list[position]
    else:
        day_in_future = ''

    if day_in_future != '' and add_numb_of_days > 1:
        time = hour_str + ':' + min_str + ' ' + meridiem + ', ' + day_in_future + ' (' + str(add_numb_of_days) + ' days later)'
        return time
    elif day_in_future != '' and add_numb_of_days == 1:
        time = hour_str + ':' + min_str + ' ' + meridiem + ' ' + day_in_future + ' (next day)'
        return time
    elif day_in_future != '' and add_numb_of_days == 0:
        time = hour_str + ':' + min_str + ' ' + meridiem + ', ' + day_in_future
        return time
    elif day_in_future == '' and add_numb_of_days > 1:
        time = hour_str + ':' + min_str + ' ' + meridiem + ' (' + str(add_numb_of_days) + ' days later)'
        return time
    elif day_in_future == '' and add_numb_of_days == 1:
        time = hour_str + ':' + min_str + ' ' + meridiem + ' (next day)'
        return time
    else:
        time = hour_str + ':' + min_str + ' ' + meridiem
        return time


s = input("Please type a start time: ")
d = input("Please type the duration of time that passes: ")
w = input("(Optional) What is the day of the week? If not given, please type 'NA'. ")

t= add_time(s, d, w)
print(t)
