# coding=gbk
import pandas as pd
import os

out_path = '../processed/'
remove_outliter_result_path = '../remove_outliter_result/'
if __name__ == '__main__':
    file_list = []
    for item in os.listdir(remove_outliter_result_path):
        df = pd.read_csv(remove_outliter_result_path + item, encoding='gb2312')
        file_list.append(df)
    df = pd.concat(file_list)
    pearson_df = df.corr(method='pearson')
    spearman_df = df.corr(method='spearman')
    print("pearson相关系数")
    print(pearson_df)
    print("spearman相关系数")
    print(spearman_df)

    # 计算单个文件的相关系数
    # file = 'sh600300.csv'
    # df = pd.read_csv(remove_outliter_result_path + file, encoding='gb2312')
    # print("pearson相关系数")
    # print(df.corr(method='pearson'))
    # print("spearman相关系数")
    # print(df.corr(method='spearman'))