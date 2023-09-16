import schedule
from datetime import datetime, timedelta, date
import datetime
import calendar
import time

myclint = MongoClint("")
db = myclint["---"]
allocation_db = db['Allocations']

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

def refine_day_list():
    today = date.today()

    remove_date = today - timedelta(days=1)
    #print(remove_date)

    add_date = today + timedelta(days=13)
    #print(add_date)

    add_date_sting=str(add_date)
    add_date_sting=add_date_sting.split('-')
    new_string=add_date_sting[::-1]
    add_day=" ".join(new_string)

    day=findDay(add_day)

    delete_query = {'Date':remove_date}
    allocation_db.delete_one(delete_query)

    record = {'Date':add_date,'Times':day}
    allocation_db.insert_one(record)


while True:
    schedule.every().day.at("00:10").do(refine_day_list)
    time.sleep(1)