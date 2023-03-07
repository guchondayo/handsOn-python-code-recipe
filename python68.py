# breakelseの法則

# 後続の処理をスキップ
import math
l = [1,54,35,43,-1]
for x in l:
    if x < 0:
        print(f"{x}はマイナスなのでスキップします")
        break
        # ここ以降はスキップ
    else:
        print("スキップしない。breakelseの法則")
    s = math.sqrt(x)
    print(s)
