from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('customer_churn_large_dataset.csv.pkl'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        CustomerID = int(request.form['CustomerID'])
        Age = int(request.form['Age'])
       Subscription_Length_Months = int(request.form['Subscription_Length_Months'])
        Gender of Customer = int(request.form['Gender of Customer'])
        Total_Usage_GB = int(request.form['Total_Usage_GB'])
        Monthly_Bill= int(request.form['Monthly_Bill'])
        Location_Los Angeles	 = request.form['Location_Los Angeles']
        if(Location_Los Angeles	 == 'Los Angeles	'):
            Location_Los Angeles= 1
            Location_New York= 0
            Location_Miami = 0
                
        elif(Location_Los Angeles == 'Miami'):
            Location_Los Angeles = 0
            Location_Miami= 1
           Location_New York = 0
        
        else:
            Location_Los Angeles= 0
           Location_Miami= 0
           Location_New York = 1
        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain,Gender_Male]])
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)