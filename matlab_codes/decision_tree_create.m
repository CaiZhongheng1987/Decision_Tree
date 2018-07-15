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

feature_num      = size(feature_matrix,1);% ͳ���ж���������
gain_matrix      = zeros(feature_num,1);
class_data       = unique(class_matrix);%ͳ���ж����ַ��࣬�õ�ÿ�ַ���ľ���ȡֵ
class_num        = length(class_data);% ��÷������
class_num_matrix = zeros(class_num,1);

switch create_method
    case 0 % ID3
        %% ������ѵ����������һ�����࣬������ǵ����������������Ϊ�ýڵ�����ǣ�����
        if(class_num==1)
            decision_tree.slct_class = class_data;
            return;
        else
        end
        
        %% �������������Ѿ�ʹ���꣬�Ǹýڵ�Ҳ�ǵ����������ѵ����������һ��������Ϊ�ýڵ������
        if(length(discard_feature)==feature_num)
            for class_idx=1:class_num
                class_num_matrix(class_idx) = length(find(class_matrix==class_data(class_idx)));
            end
            [~,slct_class_idx]          = max(class_num_matrix);
            decision_tree.slct_class    = class_data(slct_class_idx);
            return;
        else
        end

        %% ���������������������㣬�ͼ������������Ϣ���棬ѡ����Ϣ�������������������
        for feature_idx=1:feature_num
            gain_matrix(feature_idx) = calc_information_gain(feature_matrix(feature_idx,:), class_matrix);
        end
        % �ҵ���Ϣ������������
        gain_matrix(discard_feature) = -1;% �����Ѿ�ѡ����˵��������ͽ���Ϣ��������Ϊ-1������ѡ��max��ʱ��Ͳ������
        [max_gain, max_idx]          = max(gain_matrix);
        
        if(max_gain<create_threshold)
            % ���������Ϣ���涼��С�����ޣ��Ǿ��ҵ�class_matrix�������࣬�Ը�����Ϊ�������������
            for class_idx=1:class_num
                class_num_matrix(class_idx) = length(find(class_matrix==class_data(class_idx)));
            end
            [~,slct_class_idx]          = max(class_num_matrix);
            decision_tree.slct_class    = class_data(slct_class_idx);
        else
            % ����ʹ�ø����������ɾ�������
            decision_tree.slct_class    = [];
            decision_tree.feature       = max_idx;% ȷ���ýڵ�ʹ������������������
            discard_feature             = [discard_feature; max_idx];
            decision_tree.feature_array = unique(feature_matrix(max_idx,:));% ÿ����������Щȡֵ
            for feature_array_idx=1:length(decision_tree.feature_array)
                new_feature_matrix_idx  = find(feature_matrix(max_idx,:)==decision_tree.feature_array(feature_array_idx));
                new_feature_matrix      = feature_matrix(:,new_feature_matrix_idx); % ���������Ĳ�ͬȡֵ��ѵ�������л��֣��ֱ𹹽�������
                new_class_matrix        = class_matrix(new_feature_matrix_idx);
                % �ݹ����decision_tree_create�����������Ӿ�����
                tmp_child_tree          = decision_tree_create(new_feature_matrix, new_class_matrix, create_method, discard_feature, create_threshold);
                eval(['decision_tree.child_tree_' num2str(feature_array_idx,'%d') '= tmp_child_tree;']);
            end
        end
    otherwise
        error('Please check the decision tree create method!!');
end

end

