from flask import Flask,render_template,jsonify,url_for,request,redirect
import numpy as np
from project_app.utils import SurvivalPassengers
import config


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('first.html')


@app.route('/survival',methods = ['POST','GET'])
def survival():

    if request.method == 'POST':

        Pclass = request.form['Pclass']
        Gender= request.form['Gender']
        Age= request.form['Age']
        SibSp= request.form['SibSp']
        Parch= request.form['Parch']
        Fare= request.form['Fare']
        Embarked= request.form['Embarked']

        obj = SurvivalPassengers(Pclass, Gender, Age, SibSp, Parch, Fare, Embarked)

        prediction = obj.get_survival()

        return render_template('last.html',prediction = prediction)
    # return jsonify({"Result": f"Predicted Medical Insurence Charges are : {prediction}"})

# @app.route('/survival')
# def survival_status():
#     data = request.form

#     Pclass=eval(data['Pclass'])
#     Gender=eval(data['Gender'])
#     Age= eval(data['Age'])
#     SibSp= eval(data['SibSp'])
#     Parch= eval(data['Parch'])
#     Fare=eval(data['Fare'])
#     Embarked=eval(data['Embarked'])

#     obj = SurvivalPassengers(Pclass, Gender, Age, SibSp, Parch, Fare, Embarked)

#     result = obj.get_survival()

#     dict1 = {0:'The passenger would Not survived',1:"The passenger would be Survived"}

#     return dict1[result]



if __name__ =='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)