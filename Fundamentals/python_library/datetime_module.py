from datetime import date

# in date you must insert three element it's nessasery
word_cup_2022 = date(2022, 11, 21)
print(word_cup_2022)
print(word_cup_2022.day)
print(word_cup_2022.year)
print(word_cup_2022.month)

# to get the today date
today = date.today()
print(f"the today date is :{today}")
# this denpend on the number of day in the year during calcolator
same_day = date.fromordinal(748252)
print(same_day)
another_day = date.fromisoformat("2023-02-10")
print(another_day)

# to use math operation with date
from_barth_myson = today - date(2023, 2, 10)
print(from_barth_myson)
print("=" * 35)
from datetime import time

# not nessacery to insert any thing in brackets as date
time1 = time()
print(time1.hour)
print(time1.minute)
print(time1.second)

time2 = time(hour=9, minute=50, second=45)
print(time2)

time3 = time.fromisoformat("06:50:34")
print(time3)
print("=" * 38)

# to use date and time in the same time
from datetime import datetime

word_cup_2022 = datetime(year=2022, month=11, day=21, hour=13, minute=0, second=0)
print(word_cup_2022)

now = datetime.now()
print(f"the time now is :{now}")

today = datetime.today()
print(today)

count_up = now - word_cup_2022
print(count_up)
print("-" * 38)

from datetime import timedelta

delta = timedelta(days=30, weeks=7, seconds=20, minutes=57, hours=5)
print(delta)
print(now.strftime("%A, %d/%B/%Y"))
# the following code use to show the format of  time and date
print(now.strftime("%A , %d/%b/%Y, %I:%M:%S %p"))
