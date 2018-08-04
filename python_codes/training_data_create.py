"""
name   :       training_data create
author :       CaiZhongheng

date           version          record
2018.07.15     v1.0             init
2018.08.04     v1.1             数据集替换为西瓜数据集2.0
"""

# # training data
# training_data_0 = {
#     'age': 'young',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'general',
#     'loan_decision': 'no'
#     }
# training_data_1 = {
#     'age': 'young',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'good',
#     'loan_decision': 'no'
#     }
# training_data_2 = {
#     'age': 'young',
#     'job_status': 'employed',
#     'house_status': 'no_house',
#     'loan_status': 'good',
#     'loan_decision': 'yes'
#     }
# training_data_3 = {
#     'age': 'young',
#     'job_status': 'employed',
#     'house_status': 'have_house',
#     'loan_status': 'general',
#     'loan_decision': 'yes'
#     }
# training_data_4 = {
#     'age': 'young',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'general',
#     'loan_decision': 'no'
#     }
# training_data_5 = {
#     'age': 'middle',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'general',
#     'loan_decision': 'no'
#     }
# training_data_6 = {
#     'age': 'middle',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'good',
#     'loan_decision': 'no'
#     }
# training_data_7 = {
#     'age': 'middle',
#     'job_status': 'employed',
#     'house_status': 'have_house',
#     'loan_status': 'good',
#     'loan_decision': 'yes'
#     }
# training_data_8 = {
#     'age': 'middle',
#     'job_status': 'unemployed',
#     'house_status': 'have_house',
#     'loan_status': 'excellent',
#     'loan_decision': 'yes'
#     }
# training_data_9 = {
#     'age': 'middle',
#     'job_status': 'unemployed',
#     'house_status': 'have_house',
#     'loan_status': 'excellent',
#     'loan_decision': 'yes'
#     }
# training_data_10 = {
#     'age': 'old',
#     'job_status': 'unemployed',
#     'house_status': 'have_house',
#     'loan_status': 'excellent',
#     'loan_decision': 'yes'
#     }
# training_data_11 = {
#     'age': 'old',
#     'job_status': 'unemployed',
#     'house_status': 'have_house',
#     'loan_status': 'good',
#     'loan_decision': 'yes'
#     }
# training_data_12 = {
#     'age': 'old',
#     'job_status': 'employed',
#     'house_status': 'no_house',
#     'loan_status': 'good',
#     'loan_decision': 'yes'
#     }
# training_data_13 = {
#     'age': 'old',
#     'job_status': 'employed',
#     'house_status': 'no_house',
#     'loan_status': 'excellent',
#     'loan_decision': 'yes'
#     }
# training_data_14 = {
#     'age': 'old',
#     'job_status': 'unemployed',
#     'house_status': 'no_house',
#     'loan_status': 'general',
#     'loan_decision': 'no'
#     }


# training_data = []
# for idx in range(0, 15):
#     training_data.append(eval('training_data_' + str(idx)))


def create_data_set():
    """
    创建测试的数据集
    :return:
    """
    data_set = [
        # 1
        ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
        # 2
        ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
        # 3
        ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
        # 4
        ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
        # 5
        ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
        # 6
        ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '好瓜'],
        # 7
        ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '好瓜'],
        # 8
        ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '好瓜'],

        # ----------------------------------------------------
        # 9
        ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜'],
        # 10
        ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '坏瓜'],
        # 11
        ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '坏瓜'],
        # 12
        ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '坏瓜'],
        # 13
        ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '坏瓜'],
        # 14
        ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '坏瓜'],
        # 15
        ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '坏瓜'],
        # 16
        ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '坏瓜'],
        # 17
        ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜']
    ]

    # 特征值列表
    labels = ['色泽', '根蒂', '敲击', '纹理', '脐部', '触感', '决策']

    # 特征对应的所有可能的情况
    # labels_full = {}
    tmp_data = []
    tmp_dict = dict()

    for idx in range(len(data_set)):
        data_set_value = data_set[idx]
        for label_idx in range(len(labels)):
            tmp_dict[labels[label_idx]] = data_set_value[label_idx]

        tmp_data.append(tmp_dict)
        tmp_dict = dict()

    return tmp_data


training_data = create_data_set()

# for data in training_data:
#     print(data['决策'])
