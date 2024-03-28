# placeholder for any manual cofiguration we want to specify , also for values for hyper parameter tunning, paths, features etc.

import pathlib
import os
import prediction_model

#prediction_model.__file__ returns path to __init__.py file in a package
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

TRAIN_FILE = "train.csv"

TEST_FILE =  "test.csv"

MODEL_NAME='classfication.pkl'

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')

TARGET = 'Loan_Status'


#Final features used in our model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','ApplicantIncome', 'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = [ 'ApplicantIncome', 'LoanAmount',
           'Loan_Amount_Term' ]

CAT_FEATURES = ['Gender', 'Married', 'Dependents','Education',
           'Self_Employed', 'Credit_History','Property_Area' ]

# In our case it is same as categorical features
FEATURES_TO_ENCODE=['Gender', 'Married', 'Dependents','Education',
           'Self_Employed', 'Credit_History','Property_Area' ]

FEATURE_TO_MODIFY=['ApplicantIncome']
FEATURE_TO_ADD= ['CoapplicantIncome']

DROP_FEATURES=['CoapplicantIncome']

LOG_FEATURES=['ApplicantIncome', 'LoanAmount'] # TAKING LOG OF NUMERICAL FEATUERS

