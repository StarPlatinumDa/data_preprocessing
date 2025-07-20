import pandas as pd
import os

# data_path = '../data/'
out_path = '../processed/'

if __name__ == '__main__':
    numeric_field = ['开盘价', '最高价', '最低价', '收盘价', '前收盘价', '成交量', '成交额']
    cnt_wrong_date = 0
    cnt_null = 0
    cnt_outliers = 0
    for item in os.listdir(out_path):
        df = pd.read_csv(out_path + item, encoding='gb2312')
        # 判断股票名称或代码是否存在不一致
        if not (df['股票名称'] == df.loc[0,'股票名称']).all() or not (df['股票代码'] == df.loc[0,'股票代码']).all():
            print('名称或代码不一致：', df.loc[0,'股票代码'])
        # 判断是否有空值
        if df[numeric_field].isnull().values.any():
            print('有空值：', df.loc[0, '股票代码'])
            cnt_null += 1
        # 判断日期格式是否有误
        if not df['交易日期'].str.contains(pat = '^(19|20)\d\d[-/](0[1-9]|1[012]|[1-9])[-/](0[1-9]|[12][0-9]|3[01]|[1-9])$', regex = True).all():
            print("日期格式有误：", df.loc[0, '股票代码'])
            cnt_wrong_date += 1
    print(cnt_wrong_date)
    print(cnt_null)