# 凱薩密碼：將字母平移N位
# ASCII碼對照：小寫chr(97) = a , ord('a') = 97 ~ chr(122) = z , ord('z') = 12

# 0 1 2 3 4 5 6 7 8 9 ...... 25
# a b c d e f g h i j ......  z

#      +4(平移4)
# 0 1 2 3 a b c d e f
# w x y z

# a : 0 + 4 = 4
# z : 25 + 4 = 29 % 26 = 3

move = 4
i = 0
for i in range(26):
    new = ((i + move )% 26)
    print(chr(97 + i), ">", chr(97 + new)) #a~z

move = int(input("請輸入欲移動幅度："))
i = 0
for i in range(26):
    new = ((i + move )% 26)
    print(chr(97 + i), ">", chr(97 + new)) #a~z

