
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://anurag:anu@jigsaw.t1lphpq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.database

# Created or Switched to collection names
collection = db.funky
  

emp_rec1 = {
                'Phone':7384912650,
                'Name': 'Aarav Sharma',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Allergist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'12-15', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec2 = {
                'Phone':6048279135,
                'Name': 'Riya Patel',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Allergist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'9-11','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-13', 'Sunday':''} 
        }
emp_rec3 = {
                'Phone':2150496837,
                'Name': 'Krish Singh',
                'Designation and year of experience ': 'MD 15 yrs',
                'Department': 'Allergist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'15-18', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'13-14', 'Saturday':'', 'Sunday':''} 
        }
emp_rec4 = {
                'Phone':9763820415,
                'Name': 'Aanya Gupta',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Allergist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'8-9',  'Friday':'', 'Saturday':'20-23', 'Sunday':''} 
        }
emp_rec5 = {
                'Phone':3287649150,
                'Name': 'Advait Kumar',
                'Designation and year of experience ': 'MBBS 10 yrs',
                'Department': 'Allergist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'17-19','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'4-8'} 
        }
emp_rec6 = {
                'Phone':5092178463,
                'Name': 'Ananya Desai',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Allergist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-2', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'6-7', 'Saturday':'', 'Sunday':''} 
        }
emp_rec7 = {
                'Phone':1234567890,
                'Name': 'Arjun Mehta',
                'Designation and year of experience ': 'MBBS 11 yrs',
                'Department': 'Allergist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'8-9','Wednesday':'0-3', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec8 = {
                'Phone':7845019263,
                'Name': 'Isha Verma',
                'Designation and year of experience ': 'DM 22 yrs',
                'Department': 'Cardiologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'14-18','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-13', 'Sunday':''} 
        }
emp_rec9 = {
                'Phone':3658924710,
                'Name': 'Aryan Shah',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Cardiologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'8-11', 'Tuesday':'','Wednesday':'', 'Thursday':'16-20',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec10 = {
                'Phone':6927384105,
                'Name': 'Nisha Choudhury',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Cardiologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'14-16', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'13-15'} 
        }
emp_rec11 = {
                'Phone':8475092163,
                'Name': 'Devan Joshi',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Cardiologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-3', 'Tuesday':'','Wednesday':'', 'Thursday':'3-7',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec12 = {
                'Phone':2150496837,
                'Name': 'Priya Kapoor',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Cardiologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'6-9','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-12', 'Sunday':''} 
        }
emp_rec13 = {
                'Phone':5019263847,
                'Name': 'Vivaan Reddy',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Cardiologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'11-14', 'Thursday':'',  'Friday':'0-4', 'Saturday':'', 'Sunday':''} 
        }
emp_rec14 = {
                'Phone':9763287641,
                'Name': 'Meera Khanna',
                'Designation and year of experience ': 'MBBS 5 yrs',
                'Department': 'Cardiologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'5-8', 'Sunday':'0-5'} 
        }
emp_rec15 = {
                'Phone':6837491025,
                'Name': 'Kabir Malhotra',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Dermatologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'10-13', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec16 = {
                'Phone':4210935678,
                'Name': 'Zara Bhatia',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Dermatologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'11-13', 'Tuesday':'','Wednesday':'', 'Thursday':'15-19',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec17 = {
                'Phone':8102569347,
                'Name': 'Rohan Das',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Dermatologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'14-19', 'Saturday':'', 'Sunday':''} 
        }
emp_rec18 = {
                'Phone':9638745120,
                'Name': 'Tara Sharma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Dermatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-23','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'3-6', 'Sunday':''} 
        }
emp_rec19 = {
                'Phone':5709216348,
                'Name': 'Veer Singhania',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Dermatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'20-23', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'1-4'} 
        }
emp_rec20 = {
                'Phone':2468013579,
                'Name': 'Saanvi Pandey',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Dermatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'4-7', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'6-9', 'Saturday':'', 'Sunday':''} 
        }
emp_rec21 = {
                'Phone':1357924680,
                'Name': 'Virat Chawla',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Dermatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'21-23', 'Sunday':''} 
        }
emp_rec22 = {
                'Phone':9274610835,
                'Name': 'Riya Saxena',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'10-14',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec23 = {
                'Phone':4085179263,
                'Name': 'Aadi Verma',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'13-16','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-18', 'Sunday':''} 
        }
emp_rec24 = {
                'Phone':6957328140,
                'Name': 'Anika Patel',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'16-19', 'Saturday':'', 'Sunday':'10-13'} 
        }
emp_rec25 = {
                'Phone':3826497015,
                'Name': 'Arnav Kumar',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'13-18', 'Tuesday':'','Wednesday':'15-20', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec26 = {
                'Phone':8745120936,
                'Name': 'Kavya Sharma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-23','Wednesday':'', 'Thursday':'2-5',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec27 = {
                'Phone':2196837450,
                'Name': 'Advay Deshmukh',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-5', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'5-8', 'Sunday':''} 
        }
emp_rec28 = {
                'Phone':5634789012,
                'Name': 'Amaira Gupta',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'8-12', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec29 = {
                'Phone': 4071926385,  #0471926385
                'Name': 'Veer Patel',
                'Designation and year of experience ': 'DM 22 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'9-13', 'Saturday':'', 'Sunday':''} 
        }
emp_rec30 = {
                'Phone':7902163458,
                'Name': 'Siya Iyer',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-13', 'Tuesday':'','Wednesday':'13-17', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec31 = {
                'Phone':2490837615,
                'Name': 'Yuvan Rao',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'9-12','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'14-18', 'Sunday':''} 
        }
emp_rec32 = {
                'Phone':8173465920,
                'Name': 'Kiara Mehra',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'20-23', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'13-17'} 
        }
emp_rec33 = {
                'Phone':6308251947,
                'Name': 'Aarush Rathi',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'6-9','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'1-5', 'Sunday':''} 
        }
emp_rec34 = {
                'Phone':4567890123,
                'Name': 'Aanya Jain',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-5', 'Tuesday':'','Wednesday':'', 'Thursday':'10-15',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec35 = {
                'Phone':1926385740,
                'Name': 'Vihaan Bajaj',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'6-9', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'3-7'} 
        }
emp_rec36 = {
                'Phone':5839264071,
                'Name': 'Myra Singh',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Orthopedic',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'10-14'} 
        }
emp_rec37 = {
                'Phone':9368275410,
                'Name': 'Arush Kapoor',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Orthopedic',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'13-16','Wednesday':'', 'Thursday':'16-18',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec38 = {
                'Phone':2784051963,
                'Name': 'Vanya Malhotra',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Orthopedic',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'13-16', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'16-20', 'Saturday':'', 'Sunday':''} 
        }
emp_rec39 = {
                'Phone':1059283476, #0159283476
                'Name': 'Reyan Srinivasan',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Orthopedic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'20-23', 'Thursday':'',  'Friday':'', 'Saturday':'1-5', 'Sunday':''} 
        }
emp_rec40 = {
                'Phone':7045821963,
                'Name': 'Kyra Thakur',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Orthopedic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'3-7', 'Tuesday':'','Wednesday':'', 'Thursday':'7-10',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec41 = {
                'Phone':6392845071,
                'Name': 'Ayush Sharma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Orthopedic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'1-6', 'Thursday':'',  'Friday':'', 'Saturday':'21-23', 'Sunday':''} 
        }
emp_rec42 = {
                'Phone':2187465039,
                'Name': 'Anvi Agarwal',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Orthopedic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'8-12',  'Friday':'20-23', 'Saturday':'', 'Sunday':''} 
        }
emp_rec43 = {
                'Phone':5724901368,
                'Name': 'Arhaan Dasgupta',
                'Designation and year of experience ': 'DM 19 yrs',
                'Department': 'Gynecologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-14', 'Sunday':''} 
        }
emp_rec44 = {
                'Phone':9631852740,
                'Name': 'Anvi Chopra',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Gynecologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'12-14','Wednesday':'', 'Thursday':'',  'Friday':'11-13', 'Saturday':'', 'Sunday':''} 
        }
emp_rec45 = {
                'Phone':8041967325,
                'Name': 'Dhruv Mishra',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Gynecologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'13-15', 'Tuesday':'','Wednesday':'', 'Thursday':'14-19',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec46 = {
                'Phone':3178452096,
                'Name': 'Navya Kapoor',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Gynecologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'2-5', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'6-10', 'Saturday':'', 'Sunday':''} 
        }
emp_rec47 = {
                'Phone':2501639487,
                'Name': 'Ishaan Shah',
                'Designation and year of experience ': 'MBBS 10 yrs',
                'Department': 'Gynecologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'4-8',  'Friday':'', 'Saturday':'', 'Sunday':'12-17'} 
        }
emp_rec48 = {
                'Phone':8364957201,
                'Name': 'Kiara Verma',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Gynecologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'3-8', 'Thursday':'',  'Friday':'', 'Saturday':'5-9', 'Sunday':''} 
        }
emp_rec49 = {
                'Phone':5092173468,
                'Name': 'Aditya Mehra',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Gynecologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'20-23', 'Tuesday':'4-9','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec50 = {
                'Phone':1240938576,
                'Name': 'Pari Khatri',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Hepatologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'11-14',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec51 = {
                'Phone':6957201834,
                'Name': 'Arjun Patel',
                'Designation and year of experience ': 'MD 15 yrs',
                'Department': 'Hepatologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-14', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'14-18', 'Saturday':'', 'Sunday':''} 
        }
emp_rec52 = {
                'Phone':4071395826, #0471395826
                'Name': 'Sara Reddy',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Hepatologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'10-14', 'Thursday':'',  'Friday':'', 'Saturday':'11-15', 'Sunday':''} 
        }
emp_rec53 = {
                'Phone':3815729460,
                'Name': 'Neil Kapoor',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Hepatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'19-22','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'8-11'} 
        }
emp_rec54 = {
                'Phone':8240967315,
                'Name': 'Kiara Desai',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Hepatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'3-8', 'Tuesday':'','Wednesday':'', 'Thursday':'8-11',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec55 = {
                'Phone':5723019846,
                'Name': 'Krish Joshi',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Hepatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'4-8', 'Tuesday':'','Wednesday':'', 'Thursday':'1-6',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec56 = {
                'Phone':9637184520,
                'Name': 'Aisha Verma',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Hepatologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-23','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'1-6', 'Sunday':''} 
        }
emp_rec57 = {
                'Phone':9048275163,
                'Name': 'Kabir Gupta',
                'Designation and year of experience ': 'DM 24 yrs',
                'Department': 'Child Specialist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'16-18',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec58 = {
                'Phone':2154968370,
                'Name': 'Anvi Bansal',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Child Specialist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'10-13','Wednesday':'', 'Thursday':'',  'Friday':'14-18', 'Saturday':'', 'Sunday':''} 
        }
emp_rec59 = {
                'Phone':7463018259,
                'Name': 'Reyansh Sharma',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Child Specialist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'11-14', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'12-15', 'Sunday':''} 
        }
emp_rec60 = {
                'Phone':6831452079,
                'Name': 'Aahana Chopra',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Child Specialist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'10-14', 'Saturday':'', 'Sunday':'10-14'} 
        }
emp_rec61 = {
                'Phone':9325671840,
                'Name': 'Vir Patel',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Child Specialist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'20-23', 'Tuesday':'','Wednesday':'1-5', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec62 = {
                'Phone':5780149263,
                'Name': 'Anvi Iyer',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Child Specialist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'4-8', 'Saturday':'', 'Sunday':''} 
        }
emp_rec63 = {
                'Phone':7045928361,
                'Name': 'Vihaan Choudhury',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Child Specialist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'3-7','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'9-12', 'Sunday':''} 
        }
emp_rec64 = {
                'Phone':3618275940,
                'Name': 'Kiara Yadav',
                'Designation and year of experience ': 'DM 21 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'10-14', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec65 = {
                'Phone':9482637105,
                'Name': 'Aarav Malhotra',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'12-15','Wednesday':'', 'Thursday':'12-15',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec66 = {
                'Phone':2094765831,
                'Name': 'Riya Mehta',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'13-17', 'Thursday':'',  'Friday':'', 'Saturday':'10-14', 'Sunday':''} 
        }
emp_rec67 = {
                'Phone':5923178460,
                'Name': 'Aryan Kumar',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'12-16', 'Saturday':'', 'Sunday':'10-15'} 
        }
emp_rec68 = {
                'Phone':8142059376,
                'Name': 'Shanaya Bhatia',
                'Designation and year of experience ': 'MBBS 10 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'2-8', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec69 = {
                'Phone':5031789462,
                'Name': 'Krish Sharma',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'3-8', 'Saturday':'', 'Sunday':'8-11'} 
        }
emp_rec70 = {
                'Phone':7269384510,
                'Name': 'Sanya Das',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-23','Wednesday':'', 'Thursday':'',  'Friday':'14-19', 'Saturday':'', 'Sunday':''} 
        }
emp_rec71 = {
                'Phone':6957240831,
                'Name': 'Advait Joshi',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Neurologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'12-15'} 
        }
emp_rec72 = {
                'Phone':1385072964,
                'Name': 'Anika Agarwal',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Neurologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'13-18','Wednesday':'', 'Thursday':'',  'Friday':'10-15', 'Saturday':'', 'Sunday':''} 
        }
emp_rec73 = {
                'Phone':8201734659,
                'Name': 'Arnav Verma',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Neurologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'11-15', 'Tuesday':'','Wednesday':'12-16', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec74 = {
                'Phone':4976825310,
                'Name': 'Kyra Patel',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Neurologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'10-15',  'Friday':'', 'Saturday':'12-17', 'Sunday':''} 
        }
emp_rec75 = {
                'Phone':6328491705,
                'Name': 'Atharva Rao',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Neurologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'16-20', 'Tuesday':'','Wednesday':'', 'Thursday':'20-23',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec76 = {
                'Phone':5392784601,
                'Name': 'Saanvi Verma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Neurologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'10-17', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'1-6'} 
        }
emp_rec77 = {
                'Phone':9726103845,
                'Name': 'Yuvraj Kapoor',
                'Designation and year of experience ': 'MBBS 10 yrs',
                'Department': 'Neurologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'6-9', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'1-7', 'Saturday':'', 'Sunday':''} 
        }
emp_rec78 = {
                'Phone':5189374260,
                'Name': 'Siya Chawla',
                'Designation and year of experience ': 'DM 21 yrs',
                'Department': 'Osteopathic',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'10-15','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec79 = {
                'Phone':2450781963,
                'Name': 'Rishabh Khatri',
                'Designation and year of experience ': 'MD 15 yrs',
                'Department': 'Osteopathic',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'11-16', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'10-14'} 
        }
emp_rec80 = {
                'Phone':3605928147,
                'Name': 'Aarna Sharma',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Osteopathic',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-13', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'8-13', 'Saturday':'', 'Sunday':''} 
        }
emp_rec81 = {
                'Phone':4827956103,
                'Name': 'Reyansh Kumar',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Osteopathic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'9-13',  'Friday':'', 'Saturday':'10-15', 'Sunday':''} 
        }
emp_rec82 = {
                'Phone':9163847250,
                'Name': 'Aanya Iyer',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Osteopathic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'6-9', 'Saturday':'', 'Sunday':''} 
        }
emp_rec83 = {
                'Phone':5072841963, #0572841963
                'Name': 'Vihaan Deshmukh',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Osteopathic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'19-23','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'6-9', 'Sunday':''} 
        }
emp_rec84 = {
                'Phone':8396172054,
                'Name': 'Sara Gupta',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Osteopathic',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'11-16', 'Thursday':'7-11',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec85 = {
                'Phone':2163845790,
                'Name': 'Ishaan Sharma',
                'Designation and year of experience ': 'DM 19 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'12-16',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec86 = {
                'Phone':4759302168,
                'Name': 'Meher Singh',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-14', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'14-19', 'Saturday':'', 'Sunday':''} 
        }
emp_rec87 = {
                'Phone':6928475013,
                'Name': 'Arjun Khanna',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'16-20','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'12-16', 'Sunday':''} 
        }
emp_rec88 = {
                'Phone':1835724906,
                'Name': 'Vanya Reddy',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'11-16', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'10-14'} 
        }
emp_rec89 = {
                'Phone':8041259637,
                'Name': 'Kiara Choudhury',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-23','Wednesday':'', 'Thursday':'',  'Friday':'2-8', 'Saturday':'', 'Sunday':''} 
        }
emp_rec90 = {
                'Phone':4967315820,
                'Name': 'Advay Yadav',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'4-9','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'8-11'} 
        }
emp_rec91 = {
                'Phone':7325698041,
                'Name': 'Aarav Kapoor',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'6-10', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'3-9', 'Sunday':''} 
        }
emp_rec92 = {
                'Phone':5029476318, #0529476318
                'Name': 'Anvi Verma',
                'Designation and year of experience ': 'DM 22 yrs',
                'Department': 'Pediatrician',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'16-20', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec93 = {
                'Phone': 8146903275,
                'Name': 'Rehan Patel',
                'Designation and year of experience ': 'MD 19 yrs',
                'Department': 'Pediatrician',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-15', 'Tuesday':'','Wednesday':'', 'Thursday':'12-15',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec94 = {
                'Phone':6309275184,
                'Name': 'Aadya Mehta',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Pediatrician',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'12-16','Wednesday':'', 'Thursday':'',  'Friday':'13-18', 'Saturday':'', 'Sunday':''} 
        }
emp_rec95 = {
                'Phone':2578091346,
                'Name': 'Advait Singh',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Pediatrician',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-14', 'Sunday':'11-17'} 
        }
emp_rec96 = {
                'Phone':9856123470,
                'Name': 'Tara Bansal',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Pediatrician',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'1-6', 'Thursday':'',  'Friday':'5-10', 'Saturday':'', 'Sunday':''} 
        }
emp_rec97 = {
                'Phone':7314825609,
                'Name': 'Arhaan Srinivasan',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Pediatrician',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'20-23', 'Tuesday':'','Wednesday':'', 'Thursday':'17-20',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec98 = {
                'Phone':4162957830,
                'Name': 'Kyra Bhatia',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Pediatrician',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'3-9','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'5-9', 'Sunday':''} 
        }
emp_rec99 = {
                'Phone':7958631240,
                'Name': 'Aayush Patel',
                'Designation and year of experience ': 'DM 24 yrs',
                'Department': 'Phlebologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'10-15', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec100 = {
                'Phone':3627840159,
                'Name': 'Zoya Thakur',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Phlebologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'11-14', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'13-18', 'Saturday':'', 'Sunday':''} 
        }
emp_rec101 = {
                'Phone':5297840631,
                'Name': 'Krish Malhotra',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Phlebologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'14-18','Wednesday':'', 'Thursday':'10-14',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec102 = {
                'Phone':7389052164,
                'Name': 'Aahana Saxena',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Phlebologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-14', 'Sunday':'12-17'} 
        }
emp_rec103 = {
                'Phone':1409256387,
                'Name': 'Vihaan Dasgupta',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Phlebologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'8-11', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec104 = {
                'Phone':6827315940,
                'Name': 'Pari Chopra',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Phlebologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'17-20',  'Friday':'', 'Saturday':'20-23', 'Sunday':''} 
        }
emp_rec105 = {
                'Phone':9501742863,
                'Name': 'Aarav Mishra',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Phlebologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'1-6', 'Saturday':'', 'Sunday':'1-6'} 
        }
emp_rec106 = {
                'Phone':3168425079,
                'Name': 'Aaradhya Kapoor',
                'Designation and year of experience ': 'DM 26 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-14', 'Sunday':''} 
        }
emp_rec107 = {
                'Phone':7985614203,
                'Name': 'Kabir Iyer',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'10-14','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'11-16'} 
        }
emp_rec108 = {
                'Phone':4052867139,
                'Name': 'Anvi Mehra',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'13-18', 'Tuesday':'','Wednesday':'12-16', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec109 = {
                'Phone':6318425709,
                'Name': 'Advik Verma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'10-15',  'Friday':'14-18', 'Saturday':'', 'Sunday':''} 
        }
emp_rec110 = {
                'Phone':7240938561,
                'Name': 'Siya Patel',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'4-8', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec111 = {
                'Phone':5839172460,
                'Name': 'Aarna Sharma',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'8-11', 'Saturday':'20-23', 'Sunday':''} 
        }
emp_rec112 = {
                'Phone':9275610483,
                'Name': 'Rehan Bansal',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'20-13','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'1-6'} 
        }
emp_rec113 = {
                'Phone':8405217936,
                'Name': 'Arhaan Reddy',
                'Designation and year of experience ': 'DM 23 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'10-14', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec114 = {
                'Phone':5361928470,
                'Name': 'Vihaan Khanna',
                'Designation and year of experience ': 'MD 17 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'10-14', 'Tuesday':'','Wednesday':'', 'Thursday':'13-16',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec115 = {
                'Phone':9182475036,
                'Name': 'Myra Verma',
                'Designation and year of experience ': 'MD 15 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'11-15','Wednesday':'', 'Thursday':'',  'Friday':'16-20', 'Saturday':'', 'Sunday':''} 
        }
emp_rec116 = {
                'Phone':2749501638,
                'Name': 'Devansh Kapoor',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'10-13', 'Sunday':'13-17'} 
        }
emp_rec117 = {
                'Phone':6205831749,
                'Name': 'Anika Agarwal',
                'Designation and year of experience ': 'MBBS 6 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'', 'Thursday':'6-9',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec118 = {
                'Phone':4351976820,
                'Name': 'Arnav Yadav',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'18-23','Wednesday':'5-9', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec119 = {
                'Phone':8496312057,
                'Name': 'Vanya Thakur',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'12-15', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'6-11', 'Saturday':'', 'Sunday':''} 
        }
emp_rec120 = {
                'Phone':5102976843,
                'Name': 'Siya Choudhury',
                'Designation and year of experience ': 'DM 20 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'head', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'10-15'} 
        }
emp_rec121 = {
                'Phone':3968502147,
                'Name': 'Advay Mehta',
                'Designation and year of experience ': 'MD 16 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'12-15', 'Tuesday':'','Wednesday':'11-14', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec122 = {
                'Phone':2583617940,
                'Name': 'Aanya Gupta',
                'Designation and year of experience ': 'MD 18 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'sub-senior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'10-14','Wednesday':'', 'Thursday':'17-20',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec123 = {
                'Phone':6842051793,
                'Name': 'Ayansh Patel',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'12-18', 'Saturday':'11-16', 'Sunday':''} 
        }
emp_rec124 = {
                'Phone':5276938401,
                'Name': 'Kiara Iyer',
                'Designation and year of experience ': 'MBBS 9 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-6', 'Tuesday':'','Wednesday':'', 'Thursday':'20-23',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec125 = {
                'Phone':3148527906,
                'Name': 'Aaryan Malhotra',
                'Designation and year of experience ': 'MBBS 8 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'1-6','Wednesday':'17-20', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'6-9'} 
        }
emp_rec126 = {
                'Phone':6704952138,
                'Name': 'Aarohi Saxena',
                'Designation and year of experience ': 'MBBS 7 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'junior', #can also give numeric priority.
                'days':{'Monday':'1-7', 'Tuesday':'','Wednesday':'', 'Thursday':'18-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec127 = {
                'Phone':8293614750,
                'Name': 'Vihaan Das',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Allergist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec128 = {
                'Phone':9051284736,
                'Name': 'Aadhya Joshi',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Cardiologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec129 = {
                'Phone':1475829036,
                'Name': 'Shanaya Verma',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Cardiologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':'15-21'} 
        }
emp_rec130 = {
                'Phone':3984715620,
                'Name': 'Anika Mehta',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Dermatologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec131 = {
                'Phone':6152049378,
                'Name': 'Aarush Chawla',
                'Designation and year of experience ': 'MBBS 1 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec132 = {
                'Phone':7206958431,
                'Name': 'Aanya Bansal',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Endocrinologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec133 = {
                'Phone':8642597031,
                'Name': 'Neil Sharma',
                'Designation and year of experience ': 'MBBS 1 yrs',
                'Department': 'Gastroenterologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':'15-21'} 
        }
emp_rec134 = {
                'Phone':5274093168,
                'Name': 'Aarna Patel',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Gynecologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec135 = {
                'Phone':9136845270,
                'Name': 'Aarav Choudhury',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Gynecologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec136 = {
                'Phone':3704815926,
                'Name': 'Saisha Kapoor',
                'Designation and year of experience ': 'MBBS 4 yrs',
                'Department': 'Hepatologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec137 = {
                'Phone':4839201567,
                'Name': 'Advay Reddy',
                'Designation and year of experience ': 'MBBS 4 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'15-21', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec138 = {
                'Phone':7612083459,
                'Name': 'Zoya Verma',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Internal Medcine',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':'15-21'} 
        }
emp_rec139 = {
                'Phone':5947382016,
                'Name': 'Reyansh Mehta',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Neurologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec140 = {
                'Phone':2361578940,
                'Name': 'Anvi Kapoor',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Osteopathic',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec141 = {
                'Phone':8901627543,
                'Name': 'Ishaan Agarwal',
                'Designation and year of experience ': 'MBBS 5 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec142 = {
                'Phone':2159873460,
                'Name': 'Aradhya Dasgupta',
                'Designation and year of experience ': 'MBBS 4 yrs',
                'Department': 'Pediatrician',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'15-21', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec143 = {
                'Phone':6795183420,
                'Name': 'Atharv Khatri',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Pediatrician',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec144 = {
                'Phone':3275086941,
                'Name': 'Vivaan Thakur',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Phlebologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':'15-21'} 
        }
emp_rec145 = {
                'Phone':4169257380,
                'Name': 'Advait Patel',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Phlebologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec146 = {
                'Phone':9087361245,
                'Name': 'Aanya Reddy',
                'Designation and year of experience ': 'MBBS 1 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec147 = {
                'Phone':5723169840,
                'Name': 'Vihaan Srinivasan',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Pulmonologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec148 = {
                'Phone':3406928175,
                'Name': 'Kiara Bansal',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec149 = {
                'Phone':8172043965,
                'Name': 'Aarav Verma',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Rheumatologists',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec150 = {
                'Phone':6952371804,
                'Name': 'Yuvika Mehta',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Tuberculosis',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'15-21', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec151 = {
                'Phone':4296187503,
                'Name': 'Aryan Malhotra',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Orthopedic',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':'15-21'} 
        }
emp_rec152 = {
                'Phone':7584239610,
                'Name': 'Aaradhya Das',
                'Designation and year of experience ': 'MBBS 4 yrs',
                'Department': 'child specialist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec153 = {
                'Phone':1432765980,
                'Name': 'Reyansh Gupta',
                'Designation and year of experience ': 'MBBS 2 yrs',
                'Department': 'Hepatologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'', 'Thursday':'15-21',  'Friday':'', 'Saturday':'', 'Sunday':''} 
        }
emp_rec154 = {
                'Phone':9807142365,
                'Name': 'Aanya Khanna',
                'Designation and year of experience ': 'MBBS 23 yrs',
                'Department': 'Cardiologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'15-21', 'Saturday':'', 'Sunday':''} 
        }
emp_rec155 = {
                'Phone':3619857420,
                'Name': 'Kabir Patel',
                'Designation and year of experience ': 'MBBS 4 yrs',
                'Department': 'Otolaryngologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'', 'Tuesday':'15-21','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }
emp_rec156 = {
                'Phone':5402768139,
                'Name': 'Anurag Dutta',
                'Designation and year of experience ': 'MBBS 3 yrs',
                'Department': 'Neurologist',
                'Priority': 'General', #can also give numeric priority.
                'days':{'Monday':'15-21', 'Tuesday':'','Wednesday':'', 'Thursday':'',  'Friday':'', 'Saturday':'15-21', 'Sunday':''} 
        }



  
# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)
rec_id3 = collection.insert_one(emp_rec3)
rec_id4 = collection.insert_one(emp_rec4)
rec_id5 = collection.insert_one(emp_rec5)
rec_id6 = collection.insert_one(emp_rec6)
rec_id7 = collection.insert_one(emp_rec7)
rec_id8 = collection.insert_one(emp_rec8)
rec_id9 = collection.insert_one(emp_rec9)
rec_id10 = collection.insert_one(emp_rec10)
rec_id11 = collection.insert_one(emp_rec11)
rec_id12 = collection.insert_one(emp_rec12)
rec_id13 = collection.insert_one(emp_rec13)
rec_id14 = collection.insert_one(emp_rec14)
rec_id15 = collection.insert_one(emp_rec15)
rec_id16 = collection.insert_one(emp_rec16)
rec_id17 = collection.insert_one(emp_rec17)
rec_id18 = collection.insert_one(emp_rec18)
rec_id19 = collection.insert_one(emp_rec19)
rec_id20 = collection.insert_one(emp_rec20)
rec_id21 = collection.insert_one(emp_rec21)
rec_id22 = collection.insert_one(emp_rec22)
rec_id23 = collection.insert_one(emp_rec23)
rec_id24 = collection.insert_one(emp_rec24)
rec_id25 = collection.insert_one(emp_rec25)
rec_id26 = collection.insert_one(emp_rec26)
rec_id27 = collection.insert_one(emp_rec27)
rec_id28 = collection.insert_one(emp_rec28)
rec_id29 = collection.insert_one(emp_rec29)
rec_id30 = collection.insert_one(emp_rec30)
rec_id31 = collection.insert_one(emp_rec31)
rec_id32 = collection.insert_one(emp_rec32)
rec_id33 = collection.insert_one(emp_rec33)
rec_id34 = collection.insert_one(emp_rec34)
rec_id35 = collection.insert_one(emp_rec35)
rec_id36 = collection.insert_one(emp_rec36)
rec_id37 = collection.insert_one(emp_rec37)
rec_id38 = collection.insert_one(emp_rec38)
rec_id39 = collection.insert_one(emp_rec39)
rec_id40 = collection.insert_one(emp_rec40)
rec_id41 = collection.insert_one(emp_rec41)
rec_id42 = collection.insert_one(emp_rec42)
rec_id43 = collection.insert_one(emp_rec43)
rec_id44 = collection.insert_one(emp_rec44)
rec_id45 = collection.insert_one(emp_rec45)
rec_id46 = collection.insert_one(emp_rec46)
rec_id47 = collection.insert_one(emp_rec47)
rec_id48 = collection.insert_one(emp_rec48)
rec_id49 = collection.insert_one(emp_rec49)
rec_id50 = collection.insert_one(emp_rec50)
rec_id51 = collection.insert_one(emp_rec51)
rec_id52 = collection.insert_one(emp_rec52)
rec_id53 = collection.insert_one(emp_rec53)
rec_id54 = collection.insert_one(emp_rec54)
rec_id55 = collection.insert_one(emp_rec55)
rec_id56 = collection.insert_one(emp_rec56)
rec_id57 = collection.insert_one(emp_rec57)
rec_id58 = collection.insert_one(emp_rec58)
rec_id59 = collection.insert_one(emp_rec59)
rec_id60 = collection.insert_one(emp_rec60)
rec_id61 = collection.insert_one(emp_rec61)
rec_id62 = collection.insert_one(emp_rec62)
rec_id63 = collection.insert_one(emp_rec63)
rec_id64 = collection.insert_one(emp_rec64)
rec_id65 = collection.insert_one(emp_rec65)
rec_id66 = collection.insert_one(emp_rec66)
rec_id67 = collection.insert_one(emp_rec67)
rec_id68 = collection.insert_one(emp_rec68)
rec_id69 = collection.insert_one(emp_rec69)
rec_id70 = collection.insert_one(emp_rec70)
rec_id71 = collection.insert_one(emp_rec71)
rec_id72 = collection.insert_one(emp_rec72)
rec_id73 = collection.insert_one(emp_rec73)
rec_id74 = collection.insert_one(emp_rec74)
rec_id75 = collection.insert_one(emp_rec75)
rec_id76 = collection.insert_one(emp_rec76)
rec_id77 = collection.insert_one(emp_rec77)
rec_id78 = collection.insert_one(emp_rec78)
rec_id79 = collection.insert_one(emp_rec79)
rec_id80 = collection.insert_one(emp_rec80)
rec_id81 = collection.insert_one(emp_rec81)
rec_id82 = collection.insert_one(emp_rec82)
rec_id83 = collection.insert_one(emp_rec83)
rec_id84 = collection.insert_one(emp_rec84)
rec_id85 = collection.insert_one(emp_rec85)
rec_id86 = collection.insert_one(emp_rec86)
rec_id87 = collection.insert_one(emp_rec87)
rec_id88 = collection.insert_one(emp_rec88)
rec_id89 = collection.insert_one(emp_rec89)
rec_id90 = collection.insert_one(emp_rec90)
rec_id91 = collection.insert_one(emp_rec91)
rec_id92 = collection.insert_one(emp_rec92)
rec_id93 = collection.insert_one(emp_rec93)
rec_id94 = collection.insert_one(emp_rec94)
rec_id95 = collection.insert_one(emp_rec95)
rec_id96 = collection.insert_one(emp_rec96)
rec_id97 = collection.insert_one(emp_rec97)
rec_id98 = collection.insert_one(emp_rec98)
rec_id99 = collection.insert_one(emp_rec99)
rec_id100 = collection.insert_one(emp_rec100)
rec_id101 = collection.insert_one(emp_rec101)
rec_id102 = collection.insert_one(emp_rec102)
rec_id103 = collection.insert_one(emp_rec103)
rec_id104 = collection.insert_one(emp_rec104)
rec_id105 = collection.insert_one(emp_rec105)
rec_id106 = collection.insert_one(emp_rec106)
rec_id107 = collection.insert_one(emp_rec107)
rec_id108 = collection.insert_one(emp_rec108)
rec_id109 = collection.insert_one(emp_rec109)
rec_id110 = collection.insert_one(emp_rec110)
rec_id111 = collection.insert_one(emp_rec111)
rec_id112 = collection.insert_one(emp_rec112)
rec_id113 = collection.insert_one(emp_rec113)
rec_id114 = collection.insert_one(emp_rec114)
rec_id115 = collection.insert_one(emp_rec115)
rec_id116 = collection.insert_one(emp_rec116)
rec_id117 = collection.insert_one(emp_rec117)
rec_id118 = collection.insert_one(emp_rec118)
rec_id119 = collection.insert_one(emp_rec119)
rec_id120 = collection.insert_one(emp_rec120)
rec_id121 = collection.insert_one(emp_rec121)
rec_id122 = collection.insert_one(emp_rec122)
rec_id123 = collection.insert_one(emp_rec123)
rec_id124 = collection.insert_one(emp_rec124)
rec_id125 = collection.insert_one(emp_rec125)
rec_id126 = collection.insert_one(emp_rec126)
rec_id127 = collection.insert_one(emp_rec127)
rec_id128 = collection.insert_one(emp_rec128)
rec_id129 = collection.insert_one(emp_rec129)
rec_id130 = collection.insert_one(emp_rec130)
rec_id131 = collection.insert_one(emp_rec131)
rec_id132 = collection.insert_one(emp_rec132)
rec_id133 = collection.insert_one(emp_rec133)
rec_id134 = collection.insert_one(emp_rec134)
rec_id135 = collection.insert_one(emp_rec135)
rec_id136 = collection.insert_one(emp_rec136)
rec_id137 = collection.insert_one(emp_rec137)
rec_id138 = collection.insert_one(emp_rec138)
rec_id139 = collection.insert_one(emp_rec139)
rec_id140 = collection.insert_one(emp_rec140)
rec_id141 = collection.insert_one(emp_rec141)
rec_id142 = collection.insert_one(emp_rec142)
rec_id143 = collection.insert_one(emp_rec143)
rec_id144 = collection.insert_one(emp_rec144)
rec_id145 = collection.insert_one(emp_rec145)
rec_id146 = collection.insert_one(emp_rec146)
rec_id147 = collection.insert_one(emp_rec147)
rec_id148 = collection.insert_one(emp_rec148)
rec_id149 = collection.insert_one(emp_rec149)
rec_id150 = collection.insert_one(emp_rec150)
rec_id151 = collection.insert_one(emp_rec151)
rec_id152 = collection.insert_one(emp_rec152)
rec_id153 = collection.insert_one(emp_rec153)
rec_id154 = collection.insert_one(emp_rec154)
rec_id155 = collection.insert_one(emp_rec155)
rec_id156 = collection.insert_one(emp_rec156)





#print("Data inserted with record ids",rec_id1)
  
# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)
