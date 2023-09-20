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
    Monday={"2150496837":[0,0,0,0,0,0],"5092178463":[0,0],"3658924710":[0,0,0,0,0,0],"8475092163":[0,0,0,0],"4210935678":[0,0,0,0],
            "2468013579":[0,0,0,0,0,0],"3826497015":[0,0,0,0,0,0,0,0,0,0],"2196837450":[0,0,0,0,0,0,0,0],
            "7902163458":[0,0,0,0,0,0], "4567890123":[0,0,0,0,0,0,0,0],"2784051963":[0,0,0,0,0,0],
            "7045821963":[0,0,0,0,0,0,0,0],"8041967325":[0,0,0,0],
            "3178452096":[0,0,0,0,0,0],"5092173468":[0,0,0,0,0,0],
            "6957201834":[0,0,0,0,0,0,0,0],"8240967315":[0,0,0,0,0,0,0,0,0,0],"5723019846":[0,0,0,0,0,0,0,0],
            "7463018259":[0,0,0,0,0,0], "9325671840":[0,0,0,0,0,0],"3618275940":[0,0,0,0,0,0,0,0],
            "8142059376":[0,0,0,0,0,0,0,0,0,0],"8201734659":[0,0,0,0,0,0,0,0],"6328491705":[0,0,0,0,0,0,0,0],
            "9726103845":[0,0,0,0,0,0],"3605928147":[0,0,0,0,0,0],"9163847250":[0,0,0,0,0,0,0,0,0,0],
            "4759302168":[0,0,0,0,0,0,0,0], "7325698041":[0,0,0,0,0,0,0,0], "8146903275":[0,0,0,0,0,0,0,0,0,0],
            "7314825609":[0,0,0,0,0,0], "3627840159":[0,0,0,0,0,0], "1409256387":[0,0,0,0,0,0,0,0,0,0], "4052867139":[0,0,0,0,0,0,0,0,0,0],
            "7240938561":[0,0,0,0,0,0,0,0,0,0], "5361928470":[0,0,0,0,0,0,0,0], "6205831749":[0,0,0,0,0,0,0,0,0,0],"8496312057":[0,0,0,0,0,0],
            "3968502147":[0,0,0,0,0,0], "5276938401":[0,0,0,0,0,0,0,0,0,0], "6704952138":[0,0,0,0,0,0,0,0,0,0,0,0],
            "8293614750":[0,0,0,0,0,0,0,0,0,0,0,0], "7206958431":[0,0,0,0,0,0,0,0,0,0,0,0], "3704815926":[0,0,0,0,0,0,0,0,0,0,0,0],
            "7612083459":[0,0,0,0,0,0,0,0,0,0,0,0], "5947382016":[0,0,0,0,0,0,0,0,0,0,0,0], "8901627543":[0,0,0,0,0,0,0,0,0,0,0,0],
            "4169257380":[0,0,0,0,0,0,0,0,0,0,0,0], "3406928175":[0,0,0,0,0,0,0,0,0,0,0,0], "1432765980":[0,0,0,0,0,0,0,0,0,0,0,0],
            "5402768139":[0,0,0,0,0,0,0,0,0,0,0,0]}
    
    Tuesday={ "6048279135":[0,0,0,0], "3287649150":[0,0,0,0], "1234567890":[0,0],
             "7845019263":[0,0,0,0,0,0,0,0], "2150496837":[0,0,0,0,0,0], "9638745120": [0,0,0,0,0,0],
             "4085179263":[0,0,0,0,0,0], "8745120936":[0,0,0,0,0,0], "2490837615":[0,0,0,0,0,0],
             "6308251947":[0,0,0,0,0,0], "9368275410":[0,0,0,0,0,0], "9631852740":[0,0,0,0],
             "5092173468": [0,0,0,0,0,0,0,0,0,0], "3815729460":[0,0,0,0,0,0], "9637184520":[0,0,0,0,0,0],
             "2154968370":[0,0,0,0,0,0],"7045928361":[0,0,0,0,0,0,0,0], "9482637105":[0,0,0,0,0,0],
             "7269384510":[0,0,0,0,0,0], "1385072964":[0,0,0,0,0,0,0,0,0,0], "5189374260": [0,0,0,0,0,0,0,0,0,0],
             "5072841963":[0,0,0,0,0,0,0,0], "6928475013":[0,0,0,0,0,0,0,0], "8041259637": [0,0,0,0,0,0],
             "4967315820":[0,0,0,0,0,0,0,0,0,0], "6309275184":[0,0,0,0,0,0,0,0], "4162957830":[0,0,0,0,0,0,0,0,0,0,0,0],
             "5297840631":[0,0,0,0,0,0,0,0], "7985614203": [0,0,0,0,0,0,0,0], "9275610483":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             "9182475036":[0,0,0,0,0,0,0,0], "4351976820":[0,0,0,0,0,0,0,0,0,0], "2583617940": [0,0,0,0,0,0,0,0],
             "3148527906":[0,0,0,0,0,0,0,0,0,0], "3984715620":[0,0,0,0,0,0,0,0,0,0,0,0], "7206958431": [0,0,0,0,0,0,0,0,0,0,0,0],
             "9136845270": [0,0,0,0,0,0,0,0,0,0,0,0],"4839201567":[0,0,0,0,0,0,0,0,0,0,0,0],
             "5947382016":[0,0,0,0,0,0,0,0,0,0,0,0], "2361578940": [0,0,0,0,0,0,0,0,0,0,0,0], "8901627543":[0,0,0,0,0,0,0,0,0,0,0,0],
             "2159873460": [0,0,0,0,0,0,0,0,0,0,0,0], "6795183420": [0,0,0,0,0,0,0,0,0,0,0,0], "4169257380": [0,0,0,0,0,0,0,0,0,0,0,0],
             "8172043965":[0,0,0,0,0,0,0,0,0,0,0,0], "7584239610":[0,0,0,0,0,0,0,0,0,0,0,0], "9807142365":[0,0,0,0,0,0,0,0,0,0,0,0],
             "3619857420":[0,0,0,0,0,0,0,0,0,0,0,0]}
        
    Thursday={"9763820415":[0,0],"3658924710":[0,0,0,0,0,0,0,0],"8475092163":[0,0,0,0,0,0,0,0],
          "4210935678":[0,0,0,0,0,0,0,0],"9274610835":[0,0,0,0,0,0,0,0],"8745120936":[0,0,0,0,0,0],
          "4567890123":[0,0,0,0,0,0,0,0,0,0],"9368275410":[0,0,0,0],"7045821963":[0,0,0,0,0,0],
          "2187465039":[0,0,0,0,0,0,0,0],"8041967325":[0,0,0,0,0,0,0,0,0,0],"2501639487":[0,0,0,0,0,0,0,0],
          "1240938576":[0,0,0,0,0,0],"8240967315":[0,0,0,0,0,0],"5723019846":[0,0,0,0,0,0,0,0,0,0],
          "9048275163":[0,0,0,0],"9482637105":[0,0,0,0,0,0],"4976825310":[0,0,0,0,0,0,0,0,0,0],
          "6328491705":[0,0,0,0,0,0],"4827956103":[0,0,0,0,0,0,0,0],"8396172054":[0,0,0,0,0,0,0,0],
          "2163845790":[0,0,0,0,0,0,0,0],"8146903275":[0,0,0,0,0,0],"7314825609":[0,0,0,0,0,0],
          "5297840631":[0,0,0,0,0,0,0,0],"6827315940":[0,0,0,0,0,0],"6318425709":[0,0,0,0,0,0,0,0,0,0],
          "5361928470":[0,0,0,0,0,0],"6205831749":[0,0,0,0,0,0],"2583617940":[0,0,0,0,0,0],
          "5276938401":[0,0,0,0,0,0],"6704952138":[0,0,0,0,0,0],"8293614750":[0,0,0,0,0,0,0,0,0,0,0,0],
          "3984715620":[0,0,0,0,0,0,0,0,0,0,0,0],"5274093168":[0,0,0,0,0,0,0,0,0,0,0,0],
          "2361578940":[0,0,0,0,0,0,0,0,0,0,0,0],"3275086941":[0,0,0,0,0,0,0,0,0,0,0,0],
          "5723169840":[0,0,0,0,0,0,0,0,0,0,0,0],"4296187503":[0,0,0,0,0,0,0,0,0,0,0,0],
          "1432765980":[0,0,0,0,0,0,0,0,0,0,0,0]}


    Friday={"2150496837":[0,0],"5092178463":[0,0],"5019263847":[0,0,0,0,0,0,0,0],
            "8102569347":[0,0,0,0,0,0,0,0,0,0],"2468013579":[0,0,0,0,0,0],"6957328140":[0,0,0,0,0,0],
            "4071926385":[0,0,0,0,0,0,0,0],"2784051963":[0,0,0,0,0,0,0,0],"2187465039":[0,0,0,0,0,0],
            "9631852740":[0,0,0,0],"3178452096":[0,0,0,0,0,0,0,0],"6957201834":[0,0,0,0,0,0,0,0],
            "2154968370":[0,0,0,0,0,0,0,0],"6831452079":[0,0,0,0,0,0,0,0],"5780149263":[0,0,0,0,0,0,0,0],
            "5923178460":[0,0,0,0,0,0,0,0],"5031789462":[0,0,0,0,0,0,0,0,0,0],"7269384510":[0,0,0,0,0,0,0,0,0,0],
            "1385072964":[0,0,0,0,0,0,0,0,0,0],"9726103845":[0,0,0,0,0,0,0,0,0,0,0,0],"3605928147":[0,0,0,0,0,0,0,0,0,0],
            "9163847250":[0,0,0,0,0,0],"4759302168":[0,0,0,0,0,0,0,0,0,0],"8041259637":[0,0,0,0,0,0,0,0,0,0,0,0],
            "6309275184":[0,0,0,0,0,0,0,0,0,0],"9856123470":[0,0,0,0,0,0,0,0,0,0],"3627840159":[0,0,0,0,0,0,0,0,0,0],
            "9501742863":[0,0,0,0,0,0,0,0,0,0],"6318425709":[0,0,0,0,0,0,0,0],"5839172460":[0,0,0,0,0,0],
            "9182475036":[0,0,0,0,0,0,0,0],"8496312057":[0,0,0,0,0,0,0,0,0,0],"6842051793":[0,0,0,0,0,0,0,0,0,0,0,0],
            "6152049378":[0,0,0,0,0,0,0,0,0,0,0,0],"9136845270":[0,0,0,0,0,0,0,0,0,0,0,0],"9087361245":[0,0,0,0,0,0,0,0,0,0,0,0],
            "8172043965":[0,0,0,0,0,0,0,0,0,0,0,0],"7584239610":[0,0,0,0,0,0,0,0,0,0,0,0],"9807142365":[0,0,0,0,0,0,0,0,0,0,0,0]}
    
    Saturday={"6048279135":[0,0,0,0,0,0],"9763820415":[0,0,0,0,0,0],"7845019263":[0,0,0,0,0,0],
              "2150496837":[0,0,0,0],"9763287641":[0,0,0,0,0,0],"9638745120":[0,0,0,0,0,0],
              "1357924680":[0,0,0,0],"4085179263":[0,0,0,0,0,0],"2196837450":[0,0,0,0,0,0],
              "2490837615":[0,0,0,0,0,0,0,0],"6308251947":[0,0,0,0,0,0,0,0],"1059283476":[0,0,0,0,0,0,0,0],
              "6392845071":[0,0,0,0],"5724901368":[0,0,0,0,0,0,0,0],"8364957201":[0,0,0,0,0,0,0,0],
              "4071395826":[0,0,0,0,0,0,0,0],"9637184520":[0,0,0,0,0,0,0,0,0,0],"7463018259":[0,0,0,0,0,0],
              "7045928361":[0,0,0,0,0,0],"2094765831":[0,0,0,0,0,0,0,0],"4976825310":[0,0,0,0,0,0,0,0,0,0],
              "4827956103":[0,0,0,0,0,0,0,0,0,0],"5072841963":[0,0,0,0,0,0],"6928475013":[0,0,0,0,0,0,0,0],
              "7325698041":[0,0,0,0,0,0,0,0,0,0,0,0],"2578091346":[0,0,0,0,0,0,0,0],"4162957830":[0,0,0,0,0,0,0,0],
              "7389052164":[0,0,0,0,0,0,0,0],"6827315940":[0,0,0,0,0,0],"3168425079":[0,0,0,0,0,0,0,0],
              "5839172460":[0,0,0,0,0,0],"2749501638":[0,0,0,0,0,0],"6842051793":[0,0,0,0,0,0,0,0,0,0],
              "9051284736":[0,0,0,0,0,0,0,0,0,0,0,0],"1475829036":[0,0,0,0,0,0,0,0,0,0,0,0],"8642597031":[0,0,0,0,0,0,0,0,0,0,0,0],
              "3704815926":[0,0,0,0,0,0,0,0,0,0,0,0],"6795183420":[0,0,0,0,0,0,0,0,0,0,0,0],"5723169840":[0,0,0,0,0,0,0,0,0,0,0,0],
              "6952371804":[0,0,0,0,0,0,0,0,0,0,0,0],"3619857420":[0,0,0,0,0,0,0,0,0,0,0,0],"5402768139":[0,0,0,0,0,0,0,0,0,0,0,0]}
    
    Sunday={"3287649150":[0,0,0,0,0,0,0,0],"6927384105":[0,0,0,0,0,0],"9763287641":[0,0,0,0,0,0,0,0,0,0],
            "5709216348":[0,0,0,0,0,0],"6957328140":[0,0,0,0,0,0],"8173465920":[0,0,0,0,0,0,0,0],
            "1926385740":[0,0,0,0,0,0,0,0],"5839264071":[0,0,0,0,0,0,0,0],"2501639487":[0,0,0,0,0,0,0,0,0,0],
            "3815729460":[0,0,0,0,0,0],"6831452079":[0,0,0,0,0,0,0,0],"5923178460":[0,0,0,0,0,0,0,0,0,0],
            "5031789462":[0,0,0,0,0,0],"6957240831":[0,0,0,0,0,0],"5392784601":[0,0,0,0,0,0,0,0,0,0],
            "2450781963":[0,0,0,0,0,0,0,0],"1835724906":[0,0,0,0,0,0,0,0],"4967315820":[0,0,0,0,0,0],
            "2578091346":[0,0,0,0,0,0,0,0,0,0,0,0],"7389052164":[0,0,0,0,0,0,0,0,0,0],"9501742863":[0,0,0,0,0,0,0,0,0,0],
            "7985614203":[0,0,0,0,0,0,0,0,0,0],"9275610483":[0,0,0,0,0,0,0,0,0,0],"2749501638":[0,0,0,0,0,0,0,0],
            "5102976843":[0,0,0,0,0,0,0,0,0,0],"3148527906":[0,0,0,0,0,0],"1475829036":[0,0,0,0,0,0,0,0,0,0,0,0],
            "8642597031":[0,0,0,0,0,0,0,0,0,0,0,0],"7612083459":[0,0,0,0,0,0,0,0,0,0,0,0],"3275086941":[0,0,0,0,0,0,0,0,0,0,0,0],
            "4296187503":[0,0,0,0,0,0,0,0,0,0,0,0]}
    
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
