def get_time(time, mode):
    m = int(time[-5:-3])
    s = int(time[-2:])
    if len(time) == 7:
        h = int(time[0])
    else:
        h = int(time[0:2])
    if mode == "s":
        return h * 60 * 60 + m * 60 + s
    elif mode == "m":
        return h * 60 + m + s / 60
    else:
        return h + m / 60 + s / 3600

print(get_time("2:00:00", "s"))
print(get_time("12:00:00", "m"))
print(get_time("1:15:00", "h"))
