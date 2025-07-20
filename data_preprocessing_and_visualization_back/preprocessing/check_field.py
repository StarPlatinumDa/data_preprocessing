import os
import pandas as pd

# data_path = '../data/'
out_path = '../processed/'
field = ['股票代码', '股票名称', '交易日期', '开盘价', '最高价', '最低价', '收盘价', '前收盘价', '成交量', '成交额']

if __name__ == '__main__':
    for item in os.listdir(out_path):
        df = pd.read_csv(out_path + item, encoding='gb2312')
        for i in df.columns.values:
            if i not in field:
                print(i, item)
                break