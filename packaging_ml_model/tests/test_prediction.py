import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_prediction

# 1. output from predict script not null
# 2. output from predict script is str data type
# 3. the output is Y for an example  data


#Fixtures ---> functions before test functions --> ensure single_prediction (to avoid multiple time exectution it ensure before executing each test these function o/p is ready so that there is no redundancy in calling)

@pytest.fixture
def single_prediction():
    test_dataset=load_dataset(config.TEST_FILE)
    single_row=test_dataset[:1]
    result = generate_prediction(single_row)
    return result


def test_single_pred_not_null(single_prediction):
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('Predictions')[0],str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get('Predictions')[0]=='Y'