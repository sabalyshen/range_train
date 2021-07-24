#這是range的練習
range(5) # [0, 1, 2, 3, 4]
range(3) # [0, 1, 2].

for d in range(3): # range通常和 forloop一起使用 
	print(d) # 將清單內容一個一個印出來
	print('hi') # 讓重複內容執行某個固定次數
game = []
game.append('GW2')
game.append('FF14')
game.append('POE')
for g in game:
    print(game[0])
    print(g)
    print('like') 
    print('like', g)

#random + range
import random

for i in range(5): # 執行5次
	r = random.randint(1, 100)
	print(r)
	print(i) # 印出range(5)裡面所有東西[0, 1, 2, 3, 4]
	print('這是第', i+1, '產生隨機數', r)