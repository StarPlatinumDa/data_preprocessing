# coding=gbk
import pandas as pd
import os

# data_path = '../data/'
out_path = '../processed/'
test_path = '../remove_outliter_result/'

if __name__ == '__main__':
    for item in os.listdir(out_path):
        df = pd.read_csv(out_path + item, encoding='gb2312')
        # yyyy/M/d
        if df['交易日期'].str.contains(pat = '^(19|20)\d\d/([1-9]|1[012])/([1-9]|[12][0-9]|3[01])$', regex = True).all():
            df = pd.read_csv(out_path + item, encoding='gb2312', parse_dates=['交易日期'])
            df.to_csv(out_path + item, encoding='gb2312', index=False)
        # dd/MM/yy
        elif df['交易日期'].str.contains(pat = '^(0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01])[/](\d\d)$', regex = True).any():
            df = pd.read_csv(out_path + item, encoding='gb2312', parse_dates=['交易日期'])
            df.to_csv(out_path + item, encoding='gb2312', index=False)