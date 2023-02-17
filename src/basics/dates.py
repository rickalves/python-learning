from datetime import datetime, timezone, timedelta


# dealing with date
now_date = datetime.today()
print(now_date)
format_date = now_date.strftime('%d/%m/%Y')
print(format_date)
format_date = now_date.strftime('%d/%m/%Y %H:%M   ')
print(format_date)

# dates from str
myniver = '20/02/1994 00:00'

niver_date = datetime.strptime(myniver, '%d/%m/%Y %H:%M')
print(datetime.strftime(niver_date, '%d/%m/%Y %H:%M'))

#timezone and date operations timedelta



time_diff = timedelta(hours=-3)
print(time_diff)

time_zone = timezone(time_diff)
print(time_zone)

date_time_zone = now_date.astimezone(time_zone) 
print(date_time_zone)



