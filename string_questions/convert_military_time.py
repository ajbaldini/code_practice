"""
Convert a normal time input in format 08:05:15PM to military time 20:05:15
"""

def timeConversion(s):
    dt = s[8:10]
    hour = int(s[0:2])

    if dt == "AM" and hour == 12:
        hour = hour - 12
    if dt == "PM" and hour != 12:
        hour = hour + 12

    ft = str(hour).zfill(2)+s[2:8]

    return ft

print(timeConversion("07:05:45PM"))
print(timeConversion("02:05:45AM"))
print(timeConversion("12:40:22AM"))