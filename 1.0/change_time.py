def get_time(time,mode):
    if len(time) == 8:
        hours = int(time[0:2])
        minutes = int(time[3:5])
        seconds = int(time[6:])
    else:
        hours = int(time[0:1])
        minutes = int(time[2:4])
        seconds = int(time[5:])
    computed_time = None
    if mode == 's':
        computed_time = hours * 3600 + minutes * 60 + seconds
    elif mode == 'm':
        computed_time = hours * 60 + minutes + round(seconds / 60, 2)
    elif mode == 'h':
        computed_time = hours + round(minutes / 60 ,2) + round(seconds / 3600, 2)

    return computed_time

print(get_time('4:50:34','s'))
print(get_time('2:00:00','s'))
print(get_time('12:00:35','m'))
print(get_time('1:15:00','h'))