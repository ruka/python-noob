# 文件读写的原始方式
with open("网络机器人/01.csv_data.csv", "w", encoding="utf-8")as f:
    f.write("姓名，年龄，班级，爱好\n")
    f.write("张三,18,1班,篮球\n")
    f.write("李四,19,2班,足球\n")
    f.write("王五,20,3班,羽毛球\n")
    f.write("赵六,21,4班,排球\n")

with open("网络机器人/csv_data.csv", "r", encoding="utf-8")as f:
    for line in f:
        print(line.strip())


# 用csv方法读写csv文件
import csv

with open("网络机器人/02.csv_data.csv", "w", encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    writer.writeheader(["姓名", "年龄", "班级", "爱好"])
    writer.writerow(["张三", "18", "1班", "篮球"])
    writer.writerow(["李四", "19", "2班", "足球"])
    writer.writerow(["王五", "20", "3班", "羽毛球"])
    writer.writerow(["赵六", "21", "4班", "排球"])

with open("网络机器人/csv_data.csv", "r", encoding="utf-8")as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
