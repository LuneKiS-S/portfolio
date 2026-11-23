import csv
lines = []
records = []
with open("week03/data/students.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = int(row["语文"]) + int(row["数学"]) + int(row["英语"])
        avg = total / 3
        lines.append(f"{row['姓名']} 总分{total} 平均{round(avg,1)}")
        records.append([row["姓名"],total,round(avg,1)])
with open("report.txt","w",encoding="utf-8")as f:
    f.write("=====成绩报告=====\n\n")
    for line in lines:
        f.write(line + "\n")
with open("week03/summary.csv","w",encoding="utf-8",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["姓名","总分","平均分"])
    writer.writerows(records)