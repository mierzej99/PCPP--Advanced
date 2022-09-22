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
            except AttributeError as e:
                tempSeconds = self.changeToSeconds() + otherTime
                tempHours = tempSeconds // (60*60)
                tempSeconds %= 60*60
                tempMinutes = tempSeconds // 60
                tempSeconds %= 60
            return Time(tempHours, tempMinutes, tempSeconds)
        def __sub__(self, otherTime):
            try:
                return self.__add__(Time(-otherTime.hours, -otherTime.minutes, -otherTime.seconds))
            except:
                return self.__add__(-otherTime)
        def __mul__(self, value):
            tempSeconds = (self.changeToSeconds()) * value
            tempHours = tempSeconds // (60*60)
            tempSeconds %= 60*60
            tempMinutes = tempSeconds // 60
            tempSeconds %= 60
            return Time(tempHours, tempMinutes, tempSeconds)
            
tti = Time(21,58,50)


print(tti + 62)
print(tti - 62) 