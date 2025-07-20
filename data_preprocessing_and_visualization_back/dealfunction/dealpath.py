import csv
def dealcsv(path):
    jso=[]
    with open('processed/'+path) as f:
        f_csv=csv.reader(f)
        head = next(f_csv)
        for line in f_csv:
            temp = {}
            num = 0
            for i in head:
                temp[str(i)] = line[num]
                num = num + 1
            jso.append(temp)
    return jso
