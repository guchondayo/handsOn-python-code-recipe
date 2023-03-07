# 重要！
# アンチパターンを改善したい
# ①連続した比較演算子をつかう:
x = 1
y = 2
z = 3

if x < y and y < z:
    print("適正範囲だけど、andはなして、繋げても良くね？")

if x < y < z:
    print("適正範囲だけど、andはなしだとスッキリするよね！")

# 複数の値判定では、inを使うこと

name = "谷口"
if name == "谷口" or name =="野村":
    print("一つの変数に対してこれかこれの時は、in（）を使うこと)")
if name in("谷口","野村"):
    print("一つの変数に対してこれかこれの時は、in（）を使うこと)")

# if flag == trueとかやりがち
# →そのまま使え
# →0とか、""はfalseになるからね
flg = True
if flg:
    print("綺麗なフラグ")

if flg == True:
    print("汚いフラグ")

# 三項演算子の活用
x = 200 if flg else 100
# →再代入を防ぐ

# シーケンスはカウンタ不要
# つまり、配列の時に、何回繰り返すの？がいらない
date = (1,2,3,4)
for i in range(len(date)):
    print(date[i],"カウンタが無駄！")

for i in date:
    print(date[i],"これだけでいいんだ")

# 同じ値なら同時に代入しよう！
# →こうなる
a = b = c =100
print(a,b,c)

# よくある使い方で空の配列に追加する方法
# ①→li=[]
# ②こんなかに→加えていく
# これが、pythonだとこんなのができる
# [for]

li = [7,22,3,6]
l2 = [i for i in li]

r1 = []

# グローバルな悩みの上書き
# sum = x = y

# 変数をいれかえるとき
# だめ×

x = 100
y = 200
print(x,y)

# の時
# 入れ替えたい時
# ①yの値を仮置きtmp
# ②tmpにxを仮置きするかどうか？
tmp = x
x = y
y = tmp
print(x,y)
# OK

xx = 100
yy = 200
print(xx,yy)
yy = xx 
print(xx,yy)
