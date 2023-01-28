from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

with open('./Family.txt', 'r') as fd:
    calendar = fd.read()

cal = Calendar()
cal.from_ical(calendar)
print(calendar)
print(cal.property_items())
