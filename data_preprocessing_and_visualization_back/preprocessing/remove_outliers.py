# coding=gbk
import pandas as pd
import os

out_path = '../processed/'
remove_outliter_result_path = '../remove_outliter_result/'
if __name__ == '__main__':
    for item in os.listdir(out_path):
        # IQR
        df = pd.read_csv(out_path + item, encoding='gb2312')
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        df_out = df[~((df < (Q1 - 2.5 * IQR)) | (df > (Q3 + 2.5 * IQR))).any(axis=1)]
        df_out.to_csv(remove_outliter_result_path + item, encoding='gb2312', index=False)

        #  Quantile-based Flooring and Capping
        # df = pd.read_csv(out_path + item, encoding='gb2312')
        # filter_df = df[['开盘价', '最高价', '最低价', '收盘价', '前收盘价', '成交量', '成交额']]
        # low = 0.05
        # high = 0.95
        # quantile_df = filter_df.quantile([low, high])
        # filter_df = filter_df.apply(lambda x: x[(x <= quantile_df.loc[high, x.name]) & (x >= quantile_df.loc[low, x.name])], axis=0)
        # filter_df = pd.concat([df[['股票代码','股票名称','交易日期']], filter_df], axis=1)
        # filter_df.dropna(inplace=True)
        # filter_df.to_csv(remove_outliter_result_path + item, encoding='gb2312', index=False)