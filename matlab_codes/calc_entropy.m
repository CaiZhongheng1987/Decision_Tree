% name   :       calc_entropy
% author :       CaiZhongheng
% describe:      calc_entropy
% input  :       class_matrix     1xN array, the N is the number of training data
%                base_num         the log base num. 2, 10, exp(1)
% output :       H_data           the entropy of data
% date           version          record
% 2018.07.15     v1.0             init

function H_data = calc_entropy(class_matrix, base_num)

if nargin<2
    base_num = 2;
end

% 初始化
len_data    = length(class_matrix);
if(len_data==0)
   error('Please check the class_matrix!!!'); 
else
end
class_data  = unique(class_matrix);% 数据集D的决策分类结果数组,比如决策结果是给贷款或者不给贷款，那该数组就包含两个值
H_data      = 0;

% 计算训练集的经验熵H(D)
for class_idx=1:length(class_data)
    class_num = length(find(class_matrix==class_data(class_idx)));
    if(class_num/len_data==0)
        H_data    = H_data - 0;% 概率为0的时候单独处理。
    else
        switch base_num
            case 2
                H_data    = H_data - class_num/len_data*log2(class_num/len_data);
            case 10
                H_data    = H_data - class_num/len_data*log10(class_num/len_data);
            case exp(1)
                H_data    = H_data - class_num/len_data*log(class_num/len_data);
            otherwise
                error('Please check the base num!!!');
        end
    end
end

end

