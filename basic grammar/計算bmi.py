# 計算BMI BMI：weight/height(m)^2

#型態：數字(整數、小數)、字串
#要注意回傳值得型態，可以回傳數字英文等等，或是有意義的0
height = float(input("請輸入你的身高"))
weight = float(input("請輸入你的體重"))
print("身高是：", height)
print("體重是：", weight)
print("bmi：", weight / (height / 100) ** 2)

BMI = weight / (height / 100) ** 2

if BMI > 25:
    print("過重")
    print("少吃多動")
elif 25 > BMI >18:
    print("正常")
else:
    print("過輕")