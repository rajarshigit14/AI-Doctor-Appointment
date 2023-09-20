
import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


def doctors_list(doctors,appointment_date,Times):

    #Checking if any allocation is done or not
    Flag=0
    x=''
    name=''
    info=[]
    #checking all the doctors for appropriate date and doctor
    for doc in doctors:
        avali_days=doc['days']

        #removing the days on which the doctor does do any visits
        l=[]
        for day in avali_days:
            if avali_days[day] == '':
                l.append(day)

        for i in l:
            del avali_days[i]

        #all avaliable days in a list for the current doctor
        day_list=list(avali_days.keys())

        add_date_sting=str(appointment_date)
        add_date_sting=add_date_sting.split('-')
        new_string=add_date_sting[::-1]
        add_day=" ".join(new_string)

        day=findDay(add_day)

        #Times is a dictionary containing allotments of all doctors of appointment_date
        #Write Times extraction code below using MongoDB

        

        appointment_list_of_doc=Times[str(doc['Phone'])]
        if day in day_list and sum(appointment_list_of_doc) < len(appointment_list_of_doc):

            #Allotment will be done with this doctor
            Flag=1

            name=doc['Name']
            info.append(name)
            Time = doc['days'][day].split('-')
            Time = int(Time[0]) #Starting hour of the Doctor. Use it to find the appointment time by adding minutes

            #Allot the appointment(setting the value 1 and then break)
            for allotment in range(len(appointment_list_of_doc)):
                if appointment_list_of_doc[allotment] == 0:
                    appointment_list_of_doc[allotment]=1
                    break
        break
    
    #Getting the alloted time as string to present in frontend
    Time = int(Time)
    count = sum(appointment_list_of_doc)-1
    if count%2 == 0:
        Time += int(count/2)
        Time = str(Time)
        x=Time+":00 - "+Time+":30"
    else:
        Time += int(count/2)
        x=Time+':30 - '+str((int(Time))+1)+':00'
    info.append(x)

    #Checking if Time alloted or not
    if Flag==1:
        return info
    else:
        return "-1"  