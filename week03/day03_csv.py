# 第 3 周 D3：CSV 文件
# 运行：python week03/day03_csv.py
#
# CSV 就是"用逗号分隔的文本表格"，Excel 能直接打开它
# 数据在 week03/data/students.csv，先打开看一眼长什么样

import csv

# ===============================================================
# 题 1：读出来看看
# 用 csv.reader 逐行打印，观察每行是什么类型
# 提示：
# with open("week03/data/students.csv", "r", encoding="utf-8", newline="") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# 注意 newline="" 必须写，否则 Windows 下会出现空行
# ===============================================================
with open("week03/data/students.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# ===============================================================
# 题 2：用 DictReader 读（推荐）
# 它会把每行变成字典，键就是表头
# 打印每个人的姓名和语文成绩
# 提示：
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["姓名"], row["语文"])
# 注意：DictReader 读出来的值都是字符串，要算数得先 int()
# ===============================================================
with open("week03/data/students.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"],row["数学"])

# ===============================================================
# 题 3：算每个人的总分和平均分
# 输出格式：
#   张三  总分 259  平均 86.3
# 提示：语文、数学、英语三个键加起来
# ===============================================================
with open("week03/data/students.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.DictReader(f)
    for row in reader:
        总分 = int(row["语文"])+int(row["数学"])+int(row["英语"])
        平均分 = 总分/3
        print(row["姓名"],"总分",总分,"平均",平均分)

# ===============================================================
# 题 4：算每科的平均分
# 输出格式：
#   语文 84.0
#   数学 82.4
#   英语 83.6
# 提示：可以用字典累加，参考昨天的字符统计
# ===============================================================
subjects = ["语文", "数学", "英语"]
totals = {"语文": 0, "数学": 0, "英语": 0}
count = 0

with open("week03/data/students.csv","r",encoding="utf-8",newline="")as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        for s in subjects:
            totals[s] += int(row[s])

for s in subjects:
    print(s, round(totals[s] / count, 4))
