


def isLeapYear(year):
  return year % 4 and (not year % 100 or year % 400) 

def daysInMonth(month, year):
    thirty_day_months = [9, 4, 6, 11]
    thirty_one_day_months = [i for i in range(1, 13) if not i in thirty_day_months and i != 2]
    if i in thirty_day_months:
        return 30
    if i in thirty_one_day_months:
        return 31
    assert(i == 2)
    if isLeapYear(year):
        return 29
    return 28

def daysInYear(year):
  return 366 if isLeapYear(year) else  365

kSunday = 0
kMonday = 1
kTuesday = 2
kWednesday = 3
kThursday = 4
kFriday = 5
kSaturday = 6

start_jan_1_1900  = kMonday
start_jan_1_1901 = (kMonday + daysInYear(1900)) % 7

first_day_of_month = []

day = start_jan_1_1901

 
for year in range (1901, 2001):
    for month in range(1,13):
        first_day_of_month.append(day)
        day = (day + daysInMonth(month, year)) % 7



print len([day for day in first_day_of_month if day == kSunday])
        
