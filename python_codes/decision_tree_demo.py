"""
name   :       decision tree demo
author :       CaiZhongheng

date           version          record
2018.07.22     v1.0             init
2018.08.04     v1.1             数据集修改为西瓜数据集2.0
"""

# import setting
from training_data_create import training_data
from decision_tree_function import decision_tree_create

# Setting
create_method = 'ID3'  # ID3, C4.5, least_square, CART
create_threshold = 0  # the threshold of decision tree


# data pre-process
used_feature_array = []
final_decision_class = '决策'
decision_tree = (decision_tree_create(training_data, create_method,
                                      create_threshold, final_decision_class, used_feature_array))


