# グローバル変数は関数では変更できないの
gro = 100
def func():
   print(gro + 100)
func()
print(gro)
# 計算しても結局戻るの

grob = 200
def funcy():
    global grob 
    grob = 300
funcy()
print(grob)
# キーポイントは一旦globalで宣言すること！
