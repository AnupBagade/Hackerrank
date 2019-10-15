import datetime
import re


def make_readable(seconds):
    # Do something
    hours = 0
    minutes = 0
    second = 0
    string_format = re.findall(r':+', str(seconds))
    if string_format:
        date_time = datetime.datetime.strptime(seconds, '%H:%M:%S').strftime('%H:%M:%S')
        return date_time
    else:
        if seconds >= 3600:
            hours = seconds // 3600
            seconds = seconds % 3600

        if seconds >= 60:
            minutes = seconds // 60
            seconds = seconds % 60

        if seconds < 60:
            second = seconds

        return '{0:0=2d}:{1:0=2d}:{2:0=2d}'.format(hours, minutes, second)


if __name__ == '__main__':
    print(make_readable(86399))
    print(make_readable(359999))
    print(make_readable('01:1:2'))
    print(make_readable('0:0:0'))
    print(make_readable(60))