import sys
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            print("In predict")

            project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))

            # Build the path to the model.py file
            model_path = os.path.join(project_dir, 'artifacts', 'model.pkl')

            # Print the path to verify
            print(f"Model path: {model_path}")
            
            # model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')

            # model_path = 'artifacts\model.pkl'
            # preprocessor_path = 'artifacts\preprocesser.pkl'

            print("Before Loading",model_path)
            model=load_object(file_path=model_path)
            print("After loading model")
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            print(features)
            data_scaled=preprocessor.transform(features)
            
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)  