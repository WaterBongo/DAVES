from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

with open('./calendar.ics', 'r') as fd:
    calendar = fd.read()

cal = Calendar()
cal = cal.from_ical(calendar)

for component in cal.walk():
   if component.name == "VEVENT":
        print("\n\n\n")
        print(component.get("name"))
        print(component.get("description"))
        print(component.get("organizer"))
        print(component.get("location"))
        print(component.decoded("dtstart"))
        print(component.decoded("dtend"))
