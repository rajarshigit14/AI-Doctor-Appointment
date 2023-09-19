def list_of_priority(length,result_df):
    list=[]
    no_of_symtoms=length
    if(no_of_symtoms<=5):
        list.extend(["GENERAL PHYSICIAN","GENERAL"])
    elif(no_of_symtoms>5 and no_of_symtoms<15):
        list.extend(["JUNIOR",result_df["Specialist"][0]])
    elif(no_of_symtoms>=15 and no_of_symtoms<20):
        list.extend(["SUB_SENIOR",result_df["Specialist"][0]])
    elif(no_of_symtoms>=20):
        list.extend(["SENIOR",result_df["Specialist"][0]])
    return list