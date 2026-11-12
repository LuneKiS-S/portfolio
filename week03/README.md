# 第 3 周：字典、文件、Excel

这周结束，你会写出第一个**能卖钱**的脚本：读一批表格 → 清洗 → 输出汇总报告。

## 七天安排

| 天 | 学什么 | 写什么 | 阅读 |
|---|---|---|---|
| D1 | 字典 `dict` | 成绩字典 + 字符统计 | [使用 dict 和 set](https://liaoxuefeng.com/books/python/basic/dict-set/index.html) |
| D2 | 文件读写 `open` / `with` | 读写 txt，统计行数 | [文件读写](https://liaoxuefeng.com/books/python/io/file/index.html) |
| D3 | CSV 文件 | 读成绩 CSV 算平均 | [Python 官方 csv 文档](https://docs.python.org/zh-cn/3/library/csv.html) |
| D4 | 综合 | 成绩报告生成器 | 无（动手为主） |
| D5 | 异常处理 `try/except` | 给前几天的脚本加保护 | [错误处理](https://liaoxuefeng.com/books/python/error-debug-test/error/index.html) |
| D6 | 第三方库 `openpyxl` | 第一次读写 Excel | [安装第三方模块](https://liaoxuefeng.com/books/python/module/install/index.html) |
| D7 | 复盘 | 整理代码 + 写周记 | 无 |

## 本周验收

- [ ] 能用字典统计一段文字里每个字出现的次数
- [ ] 能读写一个 txt 文件，中文不乱码
- [ ] 能读一个 CSV，算出每列的平均值
- [ ] 能读写一个 Excel 文件
- [ ] 提交记录 ≥ 6 条

## 本周会用到的三条命令

```powershell
# 装库
python -m pip install openpyxl

# 跑脚本
python week03/day01_dict.py

# 提交
git add .
git commit -m "W3D1: 字典练习"
git push
```
