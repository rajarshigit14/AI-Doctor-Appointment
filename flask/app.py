from flask import Flask,redirect,render_template,url_for,request
from prioritylist import list_of_priority

app=Flask(__name__)
@app.route("/")
def welcomelogin():
    return render_template('login.html')
@app.route("/submit")
def indexhomepage():
    return render_template('index.html')
@app.route("/appointment")
def appoiment():
    return render_template("Appointment.html")
@app.route("/submit2",methods=["GET","POST"])
def patient_details():
    if request.method=="POST":
        name=request.form["paitent_name"]
        age=request.form["Age"]
        phone=request.form["Ph"]
        g=request.form["gender"]
        e=request.form["email"]

        h=request.form["Height"]
        w=request.form["Weight"]
        b=request.form["blood"]
        ap=request.form["aph"]
        bmi=round(int(h)/int(w),2)
        list=[]
        multi=request.form.getlist("multiselect1")
        list.extend(multi)
        multi2=request.form.getlist("multiselect2")
        list.extend(multi2)
        multi3=request.form.getlist("multiselect3")
        list.extend(multi3)
        multi4=request.form.getlist("multiselect4")
        list.extend(multi4)
        multi5=request.form.getlist("multiselect5")
        list.extend(multi5)
        multi6=request.form.getlist("multiselect6")
        list.extend(multi6)
        print(list)
        from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    def fit_predict():
        import pandas as pd
        dataset1=pd.read_csv("D:/AI doctor project/flask/file4.csv")
        dataset1=dataset1.loc[:, dataset1.columns.notna()]
        from sklearn.preprocessing import LabelEncoder
        
        var_mod = ['Disease']
        le = LabelEncoder()
        for i in var_mod:
            dataset1[i] = le.fit_transform(dataset1[i])
        
        
        X = dataset1.drop(columns="Disease")
        y = dataset1['Disease']
        from sklearn.linear_model import LogisticRegression
        model.fit(X,y)
        test_col = []
        for col in dataset1.columns:
            if col != 'Disease':
                test_col.append(col)

        symtoms_input=list.copy()
        

        #num_inputs = int(input("Enter the number of symptoms you have: "))
        global no_of_symtoms
        no_of_symtoms=len(symtoms_input)
        test_data={}
        for column in test_col:
            test_data[column] = 1 if column in symtoms_input else 0
            test_df = pd.DataFrame(test_data, index=[0])
        predict_disease=model.predict(test_df)
        predict_disease=le.inverse_transform(predict_disease)
        
        doc_data = pd.read_csv("D:/AI doctor project/flask/Doctor_Versus_Disease.csv",encoding='latin1', names=['Disease','Specialist'])
        global result_df
        result_df = pd.DataFrame({"Disease": predict_disease})
        result_df = result_df.merge(doc_data, on='Disease', how='left')
        print(result_df["Specialist"][0])


    fit_predict()
        

        

        
        
    priority_list=list_of_priority(no_of_symtoms,result_df)
    print(priority_list)


       
        
    print(priority_list[0])
    if priority_list[0]=="GENERAL PHYSICIAN":

        return render_template("End.html",name=name,age=age,phone_no=phone,gender=g,email=e,height=h,
                           weight=w,blood=b,aph=ap,bmi=bmi,doctor="General")
    else:
        
        return render_template("End.html",name=name,age=age,phone_no=phone,gender=g,email=e,height=h,
                           weight=w,blood=b,aph=ap,bmi=bmi,doctor=result_df["Specialist"][0])





if(__name__=="__main__"):
    app.run(debug=True)
