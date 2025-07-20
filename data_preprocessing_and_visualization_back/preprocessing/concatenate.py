import os
import pandas as pd

data_path = '../data/'
# out_path = '../processed/'

if __name__ == '__main__':
    target = [item for item in os.listdir(data_path) if '_' in item]
    file_name = []
    for item in target:
        if item[0:8] not in file_name:
            file_name.append(item[0:8])
    for item in file_name:
        cat_list = []
        for one in target:
            if item in one:
                tmp = pd.read_csv(data_path + one, encoding='gb2312')
                cat_list.append(tmp)
                os.remove(data_path + one)
        pd.concat(cat_list).drop_duplicates().to_csv(data_path + item + '.csv', encoding='gb2312', index=False)