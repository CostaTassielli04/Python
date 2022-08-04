class Timer:
    def __init__(self,hour=0,minutes=0,seconds=0):
        self._hour=hour
        self._minutes=minutes
        self._seconds=seconds

    def __str__(self):
        stringa=str(self._hour)+":"+str(self._minutes)+":"+str(self._seconds)
        return stringa

    def next_second(self):
        self._seconds+=1
        if self._seconds>59:
           self._seconds=0
           self._minutes+=1
           if self._minutes>59:
              self._minutes =0
              self._hour += 1
              if self._hour>23:
                  self._hour=0

    def prev_second(self):
        self._seconds -= 1
        if self._seconds < 0:
            self._seconds = 59
            self._minutes = 59
            self._hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
