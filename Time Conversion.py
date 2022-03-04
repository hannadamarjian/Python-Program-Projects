def add_time(start, duration):


  global extra_hour, min_dur

  def fixing_hours(a, b):
    hour_sum = a + b
    if hour_sum % 12 == 0:
        hour_str = str(12)  # USE AS PART OF FINAL OUTPUT

    else:
        hour_str = str(hour_sum % 12)  # USE AS PART OF FINAL OUTPUT

    return hour_str


  def exact_minute(c):
      min_str = c*2
      return min_str


  def singular_digits(d):
      min_str = '0' + str(d)
      return min_str


  # Goal 1: focus on the HOUR implementation:

  # a.) For start time (first argument):
  hour_and_min1 = start.split(':') # create a list where the first element is the hour, the second is the minute, and the third (optional) is AM or PM.
  start_hour = int(hour_and_min1[0]) # Retrieve hour and convert it to an integer.


  # b.) For duration time (second argument):
  hour_and_min2 = duration.split(':')
  dur_hour = int(hour_and_min2[0])

  # c.) Take the sum of the two numbers. We want to divide by 12 (since that is the MAXIMUM hour value) and save the remainder. Thus, we use a modulus (% in Python language) b.
  hour_str = fixing_hours(start_hour, dur_hour)

# ------------------------------------------------ (we are still in the function) -----------------------------------

  # Goal 2: focus on the MINUTE implementation:

  # a.) For start time (first argument):
  min_and_am_or_pm = hour_and_min1[1].split(' ')
  start_min = int(min_and_am_or_pm[0])

  min_and_am_or_pm2 = hour_and_min2[1].split(' ')
  dur_min = int(min_and_am_or_pm2[0])

  # b.) Take the sum of the two numbers. We want to divide by 60 (since that is the MAXIMUM minute value) and save the remainder. Thus, we use a modulus (% in Python language) b.
  min_sum = start_min + dur_min
  if min_sum > 59:
    min_dur = (start_min + dur_min) % 60 # integer is between 1-59, inclusive.
    min_str = str(min_dur)  # convert to string for output.

    if min_str == '0':  # for numbers like 60, 120, 180, etc. (multiples of 60)
        min_str = exact_minute(min_str)  # '00' for final minute output.


    elif 1 <= min_dur <= 9:
        min_str = singular_digits(min_dur)


    else:
        min_str = min_str

    extra_hour = int(min_sum/60) # save any extra hours in memory.

    if start_hour + dur_hour + extra_hour > 12: # 11 + 2 + 1 (see Example 2 on freeCodeCamp.org)
        extra_hour2 = dur_hour + extra_hour
        hour_str = fixing_hours(start_hour, extra_hour2) # additional duration --> function call if an example like this happens: 12 + 1 or 13 + 42 or 2 + 14.

    else:
        hour_dur = start_hour + dur_hour + extra_hour # 3 + 2 = 5
        hour_str = str(hour_dur)

  else:
      min_str = str(min_sum)  # USE AS PART OF FINAL OUTPUT
      if min_str == '0':
          min_str = exact_minute(min_str) # '00' for final minute output.


      elif 1 <= min_sum <= 9:
          min_str = singular_digits(min_sum)


      else:
          min_str = min_str

  extra_hour = int(min_sum/60)  # save any extra hours in memory.
  i = 0 # used for time ranges to determine meridiem.
  total_dur_hours = dur_hour + extra_hour
  while i <= total_dur_hours:
      if (11 - start_hour < total_dur_hours and i == 0) or (start_min + dur_min >= 60 and i == 0):
          if min_and_am_or_pm[1] == 'AM': # convert from AM to PM
              min_and_am_or_pm[1] = "PM" # lists are mutable, so it is okay to change an element in the list "min_and_am_or_pm"
          else:
              min_and_am_or_pm[1] = 'AM' # keep the same meridiem value
          i += 1
      if 12*(i+1) - start_hour <= total_dur_hours <= 12*(i+2) - start_hour:
          if min_and_am_or_pm[1] == 'AM':
              min_and_am_or_pm[1] = "PM"
              i += 1
          else:
              min_and_am_or_pm[1] = "AM"
              i += 1
      else:
          break

  meridiem = min_and_am_or_pm[1]

  return hour_str, min_str, meridiem



s = input("Please type a start time: ")
d = input("Please type the duration of time that passes: ")

hour, min, AM_or_PM = add_time(s, d)
print(hour + ':' + min + ' ' + AM_or_PM)

# End goal: hour_str + other strings..... and return this value as "new_time"