import os

data_path = '../data/'
info = '数据由预测者网'

if __name__ == '__main__':
    for item in os.listdir(data_path):
        with open(data_path + item, 'r') as fin:
            data = fin.read().splitlines()
            if info in data[0]:
                data.pop(0)
        with open(data_path + item, 'w') as fout:
            data = map(lambda x: x + '\n', data)
            fout.writelines(data)