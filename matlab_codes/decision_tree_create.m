% name   :       decision_tree_create
% author :       CaiZhongheng
% describe:      using the ID3 or C4.5 method to create decision tree
% input  :       feature_matrix     MxN matrix, the M is the feature_num, the N is the number of training data
%                class_matrix       1xN array, the N is the number of training data
%                create_method      0: ID3, 1: C4.5 2: least_square 3: CART
%                discard_feature    the used feature array.
%                create_threshold   the threshold of decision tree
% output :       decision_tree      the created decision tree 
% date           version            record
% 2018.07.15     v1.0               init

function decision_tree = decision_tree_create(feature_matrix, class_matrix, create_method, discard_feature, create_threshold)

feature_num      = size(feature_matrix,1);% 统计有多少种特征
gain_matrix      = zeros(feature_num,1);
class_data       = unique(class_matrix);%统计有多少种分类，得到每种分类的具体取值
class_num        = length(class_data);% 获得分类个数
class_num_matrix = zeros(class_num,1);

switch create_method
    case 0 % ID3
        %% 若所有训练集都属于一个分类，那这就是单结点树，将该类作为该节点的类标记，返回
        if(class_num==1)
            decision_tree.slct_class = class_data;
            return;
        else
        end
        
        %% 若所有特征都已经使用完，那该节点也是单结点树，将训练集中最大的一个分类作为该节点的类标记
        if(length(discard_feature)==feature_num)
            for class_idx=1:class_num
                class_num_matrix(class_idx) = length(find(class_matrix==class_data(class_idx)));
            end
            [~,slct_class_idx]          = max(class_num_matrix);
            decision_tree.slct_class    = class_data(slct_class_idx);
            return;
        else
        end

        %% 若上面两个条件都不满足，就计算各特征的信息增益，选择信息增益最大特征划分子树
        for feature_idx=1:feature_num
            gain_matrix(feature_idx) = calc_information_gain(feature_matrix(feature_idx,:), class_matrix);
        end
        % 找到信息增益最大的特征
        gain_matrix(discard_feature) = -1;% 对于已经选择过了的特征，就将信息增益设置为-1，这样选择max的时候就不会出错
        [max_gain, max_idx]          = max(gain_matrix);
        
        if(max_gain<create_threshold)
            % 如果最大的信息增益都还小于门限，那就找到class_matrix中最大的类，以该类作为单结点树的类标记
            for class_idx=1:class_num
                class_num_matrix(class_idx) = length(find(class_matrix==class_data(class_idx)));
            end
            [~,slct_class_idx]          = max(class_num_matrix);
            decision_tree.slct_class    = class_data(slct_class_idx);
        else
            % 否则，使用该特征来生成决策子树
            decision_tree.slct_class    = [];
            decision_tree.feature       = max_idx;% 确定该节点使用哪种特征来做决策
            discard_feature             = [discard_feature; max_idx];
            decision_tree.feature_array = unique(feature_matrix(max_idx,:));% 每种特征有哪些取值
            for feature_array_idx=1:length(decision_tree.feature_array)
                new_feature_matrix_idx  = find(feature_matrix(max_idx,:)==decision_tree.feature_array(feature_array_idx));
                new_feature_matrix      = feature_matrix(:,new_feature_matrix_idx); % 根据特征的不同取值将训练集进行划分，分别构建子树。
                new_class_matrix        = class_matrix(new_feature_matrix_idx);
                % 递归调用decision_tree_create函数，生成子决策树
                tmp_child_tree          = decision_tree_create(new_feature_matrix, new_class_matrix, create_method, discard_feature, create_threshold);
                eval(['decision_tree.child_tree_' num2str(feature_array_idx,'%d') '= tmp_child_tree;']);
            end
        end
    otherwise
        error('Please check the decision tree create method!!');
end

end

