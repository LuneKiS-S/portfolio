# 第 2 周：Python 起步 + 前端第一页

两条线按 7:3 走。Python 是主线（周一、二、四、五、六），前端是副线（周三、周日）。

每天 60–90 分钟，**每天结束前提交一次**。

## 七天安排

| 天 | 线 | 学什么 | 写什么 | 文件 |
|---|---|---|---|---|
| D1 一 | Python | 变量、类型、f-string、`input` | 5 道小题 | `week02/day01.py` |
| D2 二 | Python | `if / elif / else`、比较、逻辑 | 猜数字 v1（答案写死） | `week02/day02_guess_v1.py` |
| D3 三 | 前端 | HTML 标签：`h1 p ul li img a` | 个人名片页（只有结构，没样式） | `docs/index.html` |
| D4 四 | Python | `while`、`random`、`break` | 猜数字 v2（提示大小、限 7 次） | `week02/day03_guess_v2.py` |
| D5 五 | Python | `for`、`range`、列表 | 九九表、1–100 求和、找最大 | `week02/day04_loop.py` |
| D6 六 | Python | `def`、参数、`return` | 把猜数字和成绩统计改成函数 | `week02/day05_func.py`、`week02/scores.py` |
| D7 日 | 前端 | CSS：颜色、居中、字体、圆角 | 给名片页上样式，发布到 GitHub Pages | `docs/index.html` |

## D3 的名片页长这样

新建 `docs/index.html`，内容大概是：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>LuneKiS-S</title>
</head>
<body>
  <h1>LuneKiS-S</h1>
  <p>大一 · 学 Python 和前端</p>
  <ul>
    <li>Python 自动化</li>
    <li>HTML / CSS</li>
  </ul>
  <a href="https://github.com/LuneKiS-S">我的 GitHub</a>
</body>
</html>
```

双击文件用浏览器打开，看到白底黑字的三行，就成了。**今天不管好看，只管结构。**

## 本周验收（周日自查）

- [ ] 关掉教程能写出猜数字游戏
- [ ] 成绩统计能正确处理：0 分、100 分、全不及格
- [ ] 网页能在浏览器打开，并且已经能从网上访问
- [ ] `git log --oneline` 本周至少 6 条提交

## 卡住了怎么办

1. 看报错最后一行
2. 插 `print()` 看变量到底是多少
3. 卡超过 20 分钟先跳过，记在周记里

## 资源

- Python：https://liaoxuefeng.com/books/python/
- HTML/CSS：https://developer.mozilla.org/zh-CN/docs/Learn
