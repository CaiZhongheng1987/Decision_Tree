"""
name   :       training_data create
author :       CaiZhongheng

date           version          record
2018.07.15     v1.0             init
"""

# training data
training_data_0 = {
    'age': 'young',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'general',
    'loan_decision': 'no'
    }
training_data_1 = {
    'age': 'young',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'good',
    'loan_decision': 'no'
    }
training_data_2 = {
    'age': 'young',
    'job_status': 'employed',
    'house_status': 'no_house',
    'loan_status': 'good',
    'loan_decision': 'yes'
    }
training_data_3 = {
    'age': 'young',
    'job_status': 'employed',
    'house_status': 'have_house',
    'loan_status': 'general',
    'loan_decision': 'yes'
    }
training_data_4 = {
    'age': 'young',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'general',
    'loan_decision': 'no'
    }
training_data_5 = {
    'age': 'middle',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'general',
    'loan_decision': 'no'
    }
training_data_6 = {
    'age': 'middle',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'good',
    'loan_decision': 'no'
    }
training_data_7 = {
    'age': 'middle',
    'job_status': 'employed',
    'house_status': 'have_house',
    'loan_status': 'good',
    'loan_decision': 'yes'
    }
training_data_8 = {
    'age': 'middle',
    'job_status': 'unemployed',
    'house_status': 'have_house',
    'loan_status': 'excellent',
    'loan_decision': 'yes'
    }
training_data_9 = {
    'age': 'middle',
    'job_status': 'unemployed',
    'house_status': 'have_house',
    'loan_status': 'excellent',
    'loan_decision': 'yes'
    }
training_data_10 = {
    'age': 'old',
    'job_status': 'unemployed',
    'house_status': 'have_house',
    'loan_status': 'excellent',
    'loan_decision': 'yes'
    }
training_data_11 = {
    'age': 'old',
    'job_status': 'unemployed',
    'house_status': 'have_house',
    'loan_status': 'good',
    'loan_decision': 'yes'
    }
training_data_12 = {
    'age': 'old',
    'job_status': 'employed',
    'house_status': 'no_house',
    'loan_status': 'good',
    'loan_decision': 'yes'
    }
training_data_13 = {
    'age': 'old',
    'job_status': 'employed',
    'house_status': 'no_house',
    'loan_status': 'excellent',
    'loan_decision': 'yes'
    }
training_data_14 = {
    'age': 'old',
    'job_status': 'unemployed',
    'house_status': 'no_house',
    'loan_status': 'general',
    'loan_decision': 'no'
    }


training_data = []
for idx in range(0, 15):
    training_data.append(eval('training_data_' + str(idx)))

