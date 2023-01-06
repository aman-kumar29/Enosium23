from flask import Flask,render_template,request 
import pickle 
import pandas as pd

app=Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',method=['POST'])
def predict():
    maintainance=request.form.get('peoplename')
    loan_history=request.form.get('loan_history')
    purpose=request.form.get('purpose_loan')
    loan_amount=request.form.get('loanamount')
    guarentor=request.form.get('guarantor')
    employment_year=request.form.get('employment')
    marital=request.form.get('marital')
    loan_current=request.form.get('lfcurrent')
    age=request.form.get('age')
    address=request.form.get('currentaddress')
    job=request.form.get('job')
    house=request.form.get('housing')
    property=request.form.get('property')
    duration=request.form.get('duration')
    telephone=request.form.get('telephone')
    abroad=request.form.get('abroad')
    plans=request.form.get('plans')
    installment=request.form.get('income')
    current_account=request.form.get('current_account')
    savings_account=request.form.get('savings_account') 


    li=[maintainance,loan_history,purpose,loan_amount,guarentor,employment_year,marital,loan_current,
    age,current_account,savings_account,installment,plans,abroad,telephone,duration,property,job,house,address] 
    
    model.predict([li])

    

if __name__ == '__main__':
    app.run(debug=True)
