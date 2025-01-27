# TODO: Implement Settings of a few different types.  Some  current ideas include color scheme theme, system
#   date and time for emulated games, and touchscreen calibration.

# sudo date -s "Thu Aug  9 21:31:26 UTC 2012"   # time terminal command

import os

class SystemTime:
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.weekday = ''

    def enact(self):
        self.weekday_calc()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        os.system(f'sudo date -s {self.weekday[:3]} {months[self.month - 1][:3]} {self.day} {self.hour}:{self.minute}:00 UTC {self.year}')

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0

    def weekday_calc(self):
        sum = self.year - ( self.year // 100 )
        sum += sum / 4
        months = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
        sum += self.day
        if self.is_leap_year():
            if self.month < 3:
                sum -= 1
        sum += months[self.month - 1]
        if self.year < 1900:
            if self.year < 1800:
                sum += 4
            else:
                sum += 2
        if self.year > 1999:
            sum -= 1
        weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.weekday = weekdays[sum % 7]



class SystemTheme:
    def __init__(self, bg, sel_text, menu_text, menu_button, sel_button):
        pass


class Calibration:
    def __init__(self):
        pass
