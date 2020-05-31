import jdatetime



scrape_time=jdatetime.datetime.now()

d=4
h=5

deadline_obj=scrape_time+jdatetime.timedelta(days=d,hours=h)
moment=jdatetime.datetime.now()

deadline_date=deadline_obj.strftime('%Y/%m/%d')

deadline_time=deadline_obj.strftime('%H')

print(scrape_time.strftime('%Y/%m/%d:%H'))
print(deadline_date)
print(deadline_time)


if moment > deadline_obj:
    #TODO delete record from database