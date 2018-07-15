% name   :       decision tree demo
% author :       CaiZhongheng
 
% date           version          record
% 2018.07.15     v1.0             init


%% setting
create_method       = 0; % 0: ID3, 1: C4.5 2: least_square 3: CART
create_threshold    = 0; % the threshold of decision tree

%% traing data
% age                  0: young, 1: middle aged, 2: old 
feature_matrix(1,:) = [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2];
% work status          0: no job, 1: have job
feature_matrix(2,:) = [0 0 1 1 0 0 0 1 0 0 0 0 1 1 0];
% house status         0: no house 1: have house
feature_matrix(3,:) = [0 0 0 1 0 0 0 1 1 1 1 1 0 0 0];
% loan status before   0: just so so, 1: good, 2: excellent
feature_matrix(4,:) = [0 1 1 0 0 0 1 1 2 2 2 1 1 2 0];
%                      0: do not give loan, 1: give loan. 
class_matrix        = [0 0 1 1 0 0 0 1 1 1 1 1 1 1 0];

feature_num         = size(feature_matrix,1);
len_training_data   = size(feature_matrix,2);
discard_feature     = []; % 已经选择过的特征编号，初始化的时候所有特征都可供选择，所以为空矩阵

%% create the decision tree
decision_tree       = decision_tree_create(feature_matrix, class_matrix, create_method, discard_feature, create_threshold);
