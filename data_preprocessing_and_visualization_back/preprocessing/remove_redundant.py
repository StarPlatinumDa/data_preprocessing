import os
import pandas as pd

data_path = '../data/'
out_path = '../processed/'

if __name__ == '__main__':
    for item in os.listdir(data_path):
        if item[-3:] == 'csv':
            df = pd.read_csv(data_path + item, encoding='gb2312')
            df.drop_duplicates().to_csv(out_path + item, encoding='gb2312', index=False)
        elif item[-4:] == 'json':
            df = pd.read_json(data_path + item, encoding='gb2312')
            df.drop_duplicates().to_csv(out_path + item[0:-4] + 'csv', encoding='gb2312', index=False)