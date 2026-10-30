# 第 2 周 D4：猜数字 v2 —— 循环 + 随机数
# 运行：python week02/day03_guess_v2.py
#
# 目标：答案随机，最多猜 7 次，每次提示大了/小了，猜对提前结束

import random

answer = random.randint(1, 100)
count = 0
max_count = 7
finished = False
while count < max_count:
    count += 1
    guess = int(input(f"第{count}次，输入一个1-100的数"))
    if guess == answer:
        print(f"猜对了。你用了{count}次")
        finished = True
        break
    elif guess > answer:
        print("猜大了")
    else:
        print("猜小了")
if not finished:
    print(f"次数已用尽，答案是{answer}")
# 3. 用 while 循环，让玩家反复猜
#    思路：
#      while count < max_count:
#          count += 1
#          读入 guess
#          如果猜对 → 提示 + break 跳出循环
#          如果猜大 → 提示
#          否则     → 提示
#
#    注意：break 只能跳出最内层的循环
# 4. 循环结束后，判断是猜对了还是次数用完了
#    提示：用一个变量记录"是否猜对"，比如 finished = False

print("游戏结束")
