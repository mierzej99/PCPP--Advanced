class Time:
        def __init__(self, hours, minutes, seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            
        def changeToSeconds(self):
            return self.seconds + self.minutes*60 + self.hours*60*60
            
        def __str__(self):
            return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)
        
        def __add__(self, otherTime):
            try:
                tempSeconds = self.changeToSeconds() + otherTime.changeToSeconds()
                tempHours = tempSeconds // (60*60)
                tempSeconds %= 60*60
                tempMinutes = tempSeconds // 60
                tempSeconds %= 60
                return Time(tempHours, tempMinutes, tempSeconds)
            except TypeError as e:
                print(e)
            #return Time(tempHours, tempMinutes, tempSeconds)
        def __sub__(self, otherTime):
            return self.__add__(Time(-otherTime.hours, -otherTime.minutes, -otherTime.seconds))
        def __mul__(self, value):
            tempSeconds = (self.changeToSeconds()) * value
            tempHours = tempSeconds // (60*60)
            tempSeconds %= 60*60
            tempMinutes = tempSeconds // 60
            tempSeconds %= 60
            return Time(tempHours, tempMinutes, tempSeconds)
            
fti = Time(21,58,50)
sti = Time(1,45,22)

print(fti + sti)
print(fti - sti)
print(fti * 2)