# Python provides calendar module to display Calendar.
import calendar

print("Current month is:")
cal = calendar.month(2018, 3)
print(cal)

# prcal(year) -> prints the whole calendar of the year.
calendar.prcal(2018)

# firstweekday() -> returns the first week day. It is by default 0 which specifies Monday.
print(calendar.firstweekday())

# isleap(year) -> returns a Boolean value i.e., true or false. True in case given year is leap else false.
print(calendar.isleap(2018))

# monthcalendar(year,month) -> returns the given month with each week as one list.
print(calendar.monthcalendar(2018, 3))

# prmonth(year,month) -> prints the given month of the given year.
print(calendar.prmonth(2018, 3))
