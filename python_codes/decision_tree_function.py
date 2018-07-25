from collections import Counter
import math


def decision_tree_create(training_data, create_method, create_threshold, final_decision_class, used_feature_array):
    # name   :       decision_tree_create
    # author :       CaiZhongheng
    # describe:      using the ID3 or C4.5 method to create decision tree
    # input  :       training_data          training data list, composed by dicts of each data
    #                final_decision_class   the key string of final decision class
    #                create_method          ID3, C4.5, least_square, CART
    #                used_feature_array     the used feature list
    #                create_threshold       the threshold of decision tree
    # output :       decision_tree          the created decision tree
    # date           version                record
    # 2018.07.23     v1.0                   init

    # 首先查看有多少种最终决策的分类
    class_list = []  # 从训练集中提取出的每个数据的最终决策分类组成的列表
    len_training_data = len(training_data)
    for class_idx in range(0, len_training_data):
        tmp_class_dict = training_data[class_idx]
        class_list.append(tmp_class_dict[final_decision_class])

    final_class_dict = dict(Counter(class_list))
    final_class_array = list(final_class_dict.keys())  # 有多少种最终决策的分类
    final_class_acc = list(final_class_dict.values())  # 每种分类的个数，keys和values列表中的编号顺序是一一对应的

    final_class_number = len(final_class_array)

    # 统计训练集里面一共有多少种特征，并把特征的字符串单独提取出来做一个列表
    tmp_feature = training_data[0]
    total_feature_array = list(tmp_feature.keys())
    total_feature_array.remove(final_decision_class)  # 删掉最终代表最终决策的key
    feature_number = len(total_feature_array)

    # 初始化信息增益字典
    gain_dict = {}
    # 求得训练数据的个数
    len_training_data = len(training_data)

    if create_method == 'ID3':
        # 若所有训练集都属于一个分类，那这就是单结点树，将该类作为该节点的类标记，返回
        if final_class_number == 1:
            decision_tree = TreeNode()
            decision_tree.final_decision = final_class_array[0]
            decision_tree.feature_dict = {}
            decision_tree.child_list = []
            decision_tree.feature = []

            return decision_tree

        # 若所有特征都已经使用完，那该节点也是单结点树，将训练集中最大的一个分类作为该节点的类标记
        if len(used_feature_array) == feature_number:
            max_class_idx = final_class_acc.index(max(final_class_acc))
            decision_tree = TreeNode()
            decision_tree.final_decision = final_class_array[max_class_idx]
            decision_tree.feature_dict = {}
            decision_tree.child_list = []
            decision_tree.feature = []

            return decision_tree

        # 若上面两个条件都不满足，就计算各特征的信息增益，选择信息增益最大特征划分子树

        for feature_name in total_feature_array:
            tmp_feature_array = []
            for data_idx in range(0, len_training_data):
                tmp_feature_dict = training_data[data_idx]
                tmp_feature_array.append(tmp_feature_dict[feature_name])

            gain_dict[feature_name] = calc_information_gain(tmp_feature_array, class_list)

        # 找到信息增益最大的特征
        max_feature_name = []
        max_feature_value = -1  # 熵不会小于0，所以初始值设置为-1
        for feature_name in gain_dict.keys():
            if feature_name not in used_feature_array:
                if gain_dict[feature_name] >= max_feature_value:
                    max_feature_value = gain_dict[feature_name]
                    max_feature_name = feature_name

        if max_feature_value < create_threshold:
            # 如果最大的信息增益都还小于门限，那就找到class_list中最大的类，以该类作为单结点树的类标记
            max_class_idx = final_class_acc.index(max(final_class_acc))
            decision_tree = TreeNode()
            decision_tree.final_decision = final_class_array[max_class_idx]
            decision_tree.feature_dict = {}
            decision_tree.child_list = []
            decision_tree.feature = []

            return decision_tree

        else:
            # 否则，使用该特征来生成决策子树
            used_feature_array.append(max_feature_name)  # 表明这个特征已经用过了

            tmp_feature_array = []
            for data_idx in range(0, len_training_data):
                tmp_feature_dict = training_data[data_idx]
                tmp_feature_array.append(tmp_feature_dict[max_feature_name])  # 每种特征有哪些取值

            tmp_feature_unique = list(set(tmp_feature_array))
            decision_tree = TreeNode()
            decision_tree.feature = max_feature_name
            decision_tree.child_list = []
            decision_tree.final_decision = []
            decision_tree.feature_dict = {}

            feature_unique_idx = 0

            for feature_name in tmp_feature_unique:
                new_feature_matrix_idx = [i for i, v in enumerate(tmp_feature_array) if v == feature_name]
                new_training_data = data_select(training_data, new_feature_matrix_idx)
                tmp_child_tree = (decision_tree_create(new_training_data, create_method,
                                                       create_threshold, final_decision_class, used_feature_array))
                decision_tree.add_child(tmp_child_tree)
                decision_tree.add_dict(feature_name, feature_unique_idx)
                feature_unique_idx = feature_unique_idx + 1

        return decision_tree


def calc_information_gain(feature_array, class_list):
    # name   :       calc_information_gain
    # author :       CaiZhongheng
    # describe:      calc_information_gain
    # input  :       feature_array    1xN array, the N is the number of training data
    #                class_list       1xN array, the N is the number of training data
    # output :       information_gain the calculated of information gain
    # date           version          record
    # 2018.07.15     v1.0             init

    len_class = len(class_list)
    h_data_in_a = 0  # H(D|A)
    feature_data = list(set(feature_array))
    # 计算训练集的经验熵H(D)
    h_data = calc_entropy(class_list)
    # 计算该特征对训练集D的经验条件熵H(D|A)
    for tmp_feature in feature_data:
        # 计算每一个特征的条件熵
        # 返回feature_array中所有当前特征tmp_feature所在的位置
        tmp_feature_idx = [i for i, v in enumerate(feature_array) if v == tmp_feature]
        class_in_feature_array = data_select(class_list, tmp_feature_idx)
        h_data_idx = calc_entropy(class_in_feature_array)  # 计算H(Di)
        h_data_in_a = h_data_in_a + len(tmp_feature_idx)/len_class*h_data_idx

    # g(D,A) = H(D) - H(D|A)
    information_gain = h_data - h_data_in_a
    return information_gain


def calc_entropy(class_list, log_method='log2'):
    # name   :       calc_entropy
    # author :       CaiZhongheng
    # describe:      calc_entropy
    # input  :       class_list       1xN list, the N is the number of training data
    #                log_method       the log method. 2, 10, exp(1)
    # output :       h_data           the entropy of data
    # date           version          record
    # 2018.07.23     v1.0             init

    len_data = len(class_list)
    h_data = 0

    try:
        len_data != 0
    except ZeroDivisionError:
        print('The length of class_list is not allowed to zero!!!')
    else:
        # print('The length of class_list is ok!!!')

        # class_num = list(set(class_list))  # 数据集D的决策分类结果数组,比如决策结果是给贷款或者不给贷款，那该数组就包含两个值
        final_class_dict = dict(Counter(class_list))
        final_class_array = list(final_class_dict.keys())  # 有多少种最终决策的分类
        final_class_acc = list(final_class_dict.values())

        # 计算训练集的经验熵H(D)
        for class_idx in range(0, len(final_class_array)):
            if final_class_acc[class_idx] == 0:
                h_data = h_data - 0
            else:
                if log_method == 'loge':
                    h_data = h_data - final_class_acc[class_idx] / len_data * \
                             math.log(final_class_acc[class_idx] / len_data, math.e)
                elif log_method == 'log2':
                    h_data = h_data - final_class_acc[class_idx]/len_data * \
                             math.log(final_class_acc[class_idx]/len_data, 2)
                else:  # log10
                    h_data = h_data - final_class_acc[class_idx] / len_data * \
                             math.log(final_class_acc[class_idx] / len_data, 10)

    return h_data


def data_select(input_list, select_idx):
    # name   :       data_select
    # author :       CaiZhongheng
    # describe:      data_select
    # input  :       input_list       1xN list,
    #                select_idx       the list of idx, which wanted to be selected in input_list
    # output :       select_list      the output list in select idx of input_list
    # date           version          record
    # 2018.07.25     v1.0             init
    len_idx = len(select_idx)
    select_list = []
    for tmp_idx in range(0, len_idx):
        select_list.append(input_list[select_idx[tmp_idx]])

    return select_list


class TreeNode:
    # initiate inner node
    def __int__(self, feature, feature_dict, child_list, final_decision):
        self.feature = feature
        self.feature_dict = feature_dict
        self.child_list = []
        self.final_decision = final_decision

    def add_child(self, node):
        self.child_list.append(node)

    def add_dict(self, key, value):
        self.feature_dict[key] = value

