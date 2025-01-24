# TODO: Implement Settings of a few different types.  Some  current ideas include color scheme theme, system
#   date and time for emulated games, and touchscreen calibration.

# sudo date -s "Thu Aug  9 21:31:26 UTC 2012"   # time terminal command

class SystemTime:
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
