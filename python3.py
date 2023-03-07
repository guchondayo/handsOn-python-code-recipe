# Javascriptとpythonで若干使い方が変わる
x = 100
y = 200
z = 0
def main():
    z = x + y
main()
print(z)

# if分の書き方

ifx = 100

if ifx > 1:
    print("ifで大事なのはカッコ使わない/:を使う、インデント")


# 配列の作り方はJavascriptと同じ
# forはifとそっくりです

num_list = [0,1,2,3]

for num in num_list:
    if num > 1:
        print("forで大事なのはカッコ使わない/:を使う、インデント",num)
    else:
        print("繰り返し",num)

# 処理の中身を書かないとどうなるか
# number = 1
# if number == 0:
# →エラーになる 

number = 1
if number == 1:
    pass
# 何もおこらない→pass       
