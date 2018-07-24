"""
name   :       decision tree demo
author :       CaiZhongheng

date           version          record
2018.07.22     v1.0             init
"""

# import setting
from training_data_create import training_data
from decision_tree_function import decision_tree_create

# Setting
create_method = 'ID3'  # 0: ID3, 1: C4.5 2: least_square 3: CART
create_threshold = 0  # the threshold of decision tree

# data pre-process
used_feature_array = []
final_decision_class = 'loan_decision'
decision_tree = (decision_tree_create(training_data, create_method,
                                      create_threshold, final_decision_class, used_feature_array))

