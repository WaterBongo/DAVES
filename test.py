from icalendar import Calendar, Event
from datetime import datetime

import pytz # timezone



utc = pytz.timezone('US/Pacific')

def calculate_time(event):
    start = event['DTSTART'].dt
    end = event['DTEND'].dt
    return end - start

def check_time(time, cal):
    result = True

    for component in cal.walk():
        if component.name == "VEVENT":
            d1 = utc.localize(datetime.now())      
            d1 = d1.replace(hour=0, minute=0,second=0,microsecond=0)
            

            if (time >= component.decoded("dtstart") and time < component.decoded("dtend")):                
                result = False
    return result        
            
def available_times(cal):
    _dict = dict()
    
    d1 = utc.localize(datetime.now())      
    d1 = d1.replace(hour=0, minute=0,second=0,microsecond=0)

    for x in range(0,24):
        for y in range(0,60):
            d1 = d1.replace(hour=x,minute=y,second=0,microsecond=0)
            _dict[d1] = check_time(d1, cal)
            


    return _dict

def check_duration(duration,cal):
    _dict = available_times(cal)
    finaleTimes = list()
    for x in _dict.keys():
        if (_dict[x] == True):
            d1 = x        
            canDo = True    
            for y in range(0,duration):
                _hour = d1.hour
                _minute = d1.minute + y
                if (_minute >= 60):
                    _hour += 1
                    _minute -= 60
                if (_hour <= 23):
                    d2 = d1.replace(hour= _hour,minute=_minute,second=0,microsecond=0)
                    if (_dict[d2] == False):
                        canDo = False
            if (canDo == True):
                finaleTimes.append(d1)

    return finaleTimes

with open('./calendar.ics', 'r') as fd:
    calendar = fd.read()

cal = Calendar()
cal = cal.from_ical(calendar)

totalDuration = int(input('total duration: '))
dailyDuration = int(input('daily duration: '))

_list = check_duration(30, cal)

for x in _list:
    print(x)



