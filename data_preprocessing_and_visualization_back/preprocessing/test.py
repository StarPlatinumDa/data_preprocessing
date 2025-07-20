# coding=gbk
import pandas as pd
import os

out_path = '../processed/'
remove_outliter_result_path = '../remove_outliter_result/'
if __name__ == '__main__':
    file = 'sh600297.csv'
    file2 = 'sh600400.csv'
    # sh600297
    # df = pd.read_csv(out_path + file, encoding='gb2312')
    # # print(df.columns.values)
    # filt_df = df[['开盘价', '最高价', '最低价', '收盘价', '前收盘价', '成交量', '成交额']]
    # low = 0.05
    # high = 0.95
    # quant_df = filt_df.quantile([low, high])
    # # print(quant_df)
    # filt_df = filt_df.apply(lambda x: x[(x <= quant_df.loc[high, x.name]) & (x >= quant_df.loc[high, x.name])], axis=0)
    # filt_df = pd.concat([df[['股票代码','股票名称','交易日期']], filt_df], axis=1)
    # filt_df.dropna(inplace=True)
    # filt_df.to_csv('../remove_outliter_result/' + file, encoding='gb2312', index=False)

    # 统计记录总数
    # all_len = 0
    # for item in os.listdir(remove_outliter_result_path):
    #     df = pd.read_csv(remove_outliter_result_path + item, encoding='gb2312')
    #     all_len += len(df)
    # print(all_len)

    df = pd.read_csv(out_path + file, encoding='gb2312')
    df2 = pd.read_csv(out_path + file2, encoding='gb2312')
    print(pd.concat([df,df2]))