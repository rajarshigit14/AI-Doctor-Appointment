"""Loss of apetite#
Vomiting
Loss of balance#
Chills,shivering#
Cough
Chest pain#
Loss of smell
Fatigue
Redness of eye#
Painful walking
Headache
Abdominal pain
Dizziness
Yellowing of eye
breathlessness
High fever
Back pain
Itching
Muscle pain
Blurred and distorted vision
Diarrhea
Stiff neck
Acidity
Fast heart rate
Nausea
Lethargy
Weakness in limbs(weakness)
Joint pain
Headache
Belly pain
Irregular sugar level"""
##if 
##loss of aptitite from user
list=[]
st=input("enter the symtom")
st=" "+st
list.append(st)
if st in list:
    list.extend([" vomiting"," dehydration"," dizziness"," muscle_weakness"])
print(list)
## loss of balance

if st in list:
    list.extend([" spinning_movements"," unsteadiness"," visual_disturbance"," dizziness"," muscle_weakness"])
print(list)
##chills or shivering
if st in list:
    list.extend([" shivering"," cough","mild_fever"," runny_nose"," headache"])
print(list)
#chest pain
if st in list:
    list.extend([" fast_heart_rate"," cough"," fatigue"," breathlessness"])
print(list)
#redness in eye
if st in list:
    list.extend([" visual_disturbance"," watering_from_eyes"])
print(list)
#abdominal pain
if st in list:
    list.extend([" loss_of_appetite"])
print(list)
if st in list:
    list.extend([])
