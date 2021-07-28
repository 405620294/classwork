import random
n = random.uniform(-1, 1)
print(n)

print("-------------")

#蒙利卡羅法(first))
i = 0
count = 0
discount = 0
while i <10000:
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)
	print("(", x, y, ")") #不必印，會印一萬筆
	N = float(x ** x + y ** y) #平方=(x ** 2)
	if N > 1:
		discount = (discount + 1)
		print (discount) #不必印，會印一萬筆
	else:
		count = (count + 1) 
		print(count) #不必印，會印一萬筆
	i = i + 1
print(4 * (count / 10000))

#蒙利卡羅法(修正版)
i = 0
count = 0
discount = 0
while i <1000000:
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)
	N = float(x ** 2 + y ** 2) 
	if N > 1:
		discount = (discount + 1)
	else:
		count = (count + 1) 
	i = i + 1
print("面積:",4 * (count / 1000000))

#蒙利卡羅法(老師解))
print("-----老師解-------")
inarea, outarea = 0, 0
i = 0
while i < 1000000:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        inarea = inarea + 1
    else:
        outarea = outarea + 1
    i = i + 1
ratio = inarea / (outarea + inarea)
print(inarea, outarea)
print("面積:", ratio * 4)