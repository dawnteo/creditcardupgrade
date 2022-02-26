#!/usr/bin/env python
# coding: utf-8

# In[49]:


from flask import Flask


# In[50]:


app = Flask(__name__)


# In[51]:


from flask import request, render_template
import joblib 

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases, suppcard)
        model1 = joblib.load("CCU_DT")
        pred1 = model1.predict([[purchases,suppcard]])
        if pred1 == 0:
            decision = "No"
        else: 
            decision = "Yes"
        s1 = "The score of credit card upgrade base on decision tree is " + decision
        model2 = joblib.load("CCU_Reg")
        pred2 = model1.predict([[purchases,suppcard]])
        if pred2 == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s2 = "The score of credit card upgrade base on decision tree is " + decision
        model3 = joblib.load("CCU_NN")
        pred3 = model1.predict([[purchases,suppcard]])
        if pred3 == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s3 = "The score of credit card upgrade base on decision tree is " + decision
        model4 = joblib.load("CCU_RF")
        pred4 = model1.predict([[purchases,suppcard]])
        if pred4 == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s4 = "The score of credit card upgrade base on decision tree is " + decision
        model5 = joblib.load("CCU_GB")
        pred5 = model1.predict([[purchases,suppcard]])
        if pred5 == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s5 = "The score of credit card upgrade base on decision tree is " + decision
        return(render_template("index.html",result1=s1,result2=s2,result3=s3,result4=s4,result5=s5))
    else: 
        return(render_template("index.html",result1="2",result2="2",result3="2",result4="2",result5="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()

