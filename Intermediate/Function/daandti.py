import datetime as dt

# Date

today = dt.date.today()
print("Today : ", today)

new = dt.date(2022, 5, 27)
print(new)
print("Day : ", new.day)
print("Month : ", new.month)
print("Year : ", new.year)
print("____________________\n")

# Time

tyme = dt.time(3,15,0,0000)
print("Time : ", tyme)

print("Hour : ", tyme.hour)
print("Minute : ", tyme.minute)
print("Second : ", tyme.second)
print("Microsecond : ", tyme.microsecond)
print("____________________\n")

# Date and Time

date_time = dt.datetime.now()
print("Date & Time : ", date_time)
print("____________________\n")

# Custom Date and Time

cusdt = dt.datetime(2025,5,27,23,50,55)
print(cusdt)
print("Date : ", cusdt.date())
print("Time : ", cusdt.time())
print("____________________\n")

# Check how many days Until Next New Year

nov = dt.datetime.now()
nny = dt.datetime(2025,1,1)
check = nny - nov
print(check)
print("____________________\n")

# Manipulating Date and Time to String Format using strftime().
# strftime() ==> string format time, convert date and time to string representation.

curr = dt.datetime.now()
nyu_curr = curr.strftime("%A %B %D %Y")    # %A ==> Day | %B ==> Month | %D ==> Date | %Y ==> Year
print(nyu_curr)