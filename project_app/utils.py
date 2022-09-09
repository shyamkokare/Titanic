import numpy as np
import config
import pickle


class SurvivalPassengers():

    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass=Pclass
        self.Gender=Gender
        self.Age= Age
        self.SibSp= SibSp
        self.Parch= Parch
        self.Fare=Fare
        self.Embarked=Embarked

    def load_model(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.rf_model = pickle.load(f)

        with open(config.LABEL_ENCODER_FILE_PATH,'rb') as f:
            self.label_model = pickle.load(f)

    def get_survival(self):

        self.load_model()

        self.Gender = self.label_model[0].transform([self.Gender])[0]
        self.Embarked = self.label_model[1].transform([self.Embarked])[0]

        test_array = np.array([self.Pclass,self.Gender,self.Age,self.SibSp,self.Parch,self.Fare,self.Embarked])

        outcome = self.rf_model.predict([test_array])[0]

        return outcome