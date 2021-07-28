# 資料基礎型態：數字(整數 int 、浮點數 float)
#              文字(字串 str)
#              布林值(True False)
#              空值(None)

# 取餘數：循環列隊 >> 任一範圍中循環 0~5 循環(a % 6)

#     剪刀
#   ↗    ↘
# 石頭  ←  布
#      0
#    ↗  ↘
#   2  ←  1

import random
com = random.randint(0,2)
user = int(input("0.剪刀 1.布 2.石頭 請出拳:"))

print("我:", user, "電腦:", com)

if user == (com - 1) % 3:
    print("win") # 剪刀 vs 布   0 vs 1-1= 0
                 # 布 vs 石頭   1 vs 2-1= 1
                 # 石 vs 剪刀   2 vs 0-1= -1 % 3 = 2 ( 3 * -1 = -3 + 2 = -1)
elif com == (user - 1) % 3:
    print("lose")
else:
    print("even")