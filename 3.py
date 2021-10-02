time = "12:05:45AM"
hour = time[:2]
rest = time[2:-2]
meridiam = time[-2:]
if meridiam == "PM":
    if hour == "12":
        newTime = time[:-2]
        print(newTime)
    else:
        hour = 12 + int(hour)
        newTime = f"{hour}{rest}"
        print(newTime)
else:
    if hour == "12":
        hour = "00"
        newTime = f"{hour}{rest}"
        print(newTime)
    else:
        newTime = time[:-2]
        print(newTime)