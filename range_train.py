#這是range的練習
#range 是 python 的清單產生器，最常用
range(5) # [0, 1, 2, 3, 4]
range(3) # [0, 1, 2].

for d in range(3): # range通常和 forloop一起使用 
	print(d) # 將清單內容一個一個印出來
	print(d + 1)
	print('hi') # 讓重複內容執行某個固定次數
	#SO 上面會執行3次
game = ['GW2', 'FF14', 'POE']
for g in game:# 清單有3個會執行3次
    print('like', g)

#random + range
import random

for i in range(5): # 執行5次
	r = random.randint(1, 100)
	print(r)
	print(i) # 印出range(5)裡面所有東西[0, 1, 2, 3, 4]
	print('這是第', i+1, '產生隨機數', r)

#range 應用1 : 指定範圍
range(2, 5) # 2 ~ 5的範圍 == [2, 3, 4]

#range 應用2 : 每次增加值(step)
range(2, 10, 3) # == 2 ~ 10 [2, 5, 8]
range(10, 3 , -2) # == 3 ~ 10 [10, 8, 6, 4]