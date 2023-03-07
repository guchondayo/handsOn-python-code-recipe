# 条件をつけてループをしたいとき
# →例えば番号をつけて条件をつける

# こんな感じです
l = ["ア","イ","ウ","エ","オ"]
for idx,val in enumerate(l):
    if idx % 2== 0:
        print(idx,val)
