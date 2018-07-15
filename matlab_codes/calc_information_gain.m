% name   :       calc_information_gain
% author :       CaiZhongheng
% describe:      calc_information_gain
% input  :       feature_array    1xN array, the N is the number of training data
%                class_matrix     1xN array, the N is the number of training data
% output :       information_gain the caculated of information gain
% date           version          record
% 2018.07.15     v1.0             init

function information_gain = calc_information_gain(feature_array, class_matrix)

len_data      = length(class_matrix);
H_data_in_A   = 0;
feature_data  = unique(feature_array);
% 计算训练集的经验熵H(D)
H_data        = calc_entropy(class_matrix);
% 计算该特征对训练集D的经验条件熵H(D|A)
for feature_idx=1:length(feature_data)
    % 计算每一个特征的条件熵
    class_in_feature_idx    = find(feature_array==feature_data(feature_idx));
    len_feature             = length(class_in_feature_idx);
    class_in_feature_matrix = class_matrix(class_in_feature_idx);
    H_data_idx              = calc_entropy(class_in_feature_matrix);% 计算H(Di)
    H_data_in_A             = H_data_in_A + len_feature/len_data*H_data_idx;
end
% g(D,A) = H(D) - H(D|A)
information_gain = H_data - H_data_in_A;

end

