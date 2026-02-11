import datetime
date = datetime.date(2024, 6, 1)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(14, 30, 0)
print(time)
 
now = datetime.datetime.now()
print(now)

now1 = now.strftime("%H:%M:%S %d/%m/%Y")
print(now1)