# 第 2 周 D2：猜数字 v1
# 只练 if / elif / else，答案先写死，不用 random
# 运行：python week02/day02_guess_v1.py

# 1. 答案先写死（D4 再换成随机数）
answer = 42

# 2. 让玩家输入一个数字
#    坑：input 拿到的是字符串，要 int() 转一下
guess = int(input("猜一个 1-100 的数字："))

# 3. 比较三种情况，把下面的 ... 换成你的代码
#    注意：冒号不能少，冒号后面要缩进 4 个空格
if guess > answer:
    print("猜大了")
elif guess < answer:
    print("猜小了")
else:
    print("猜对了")

print("游戏结束")
