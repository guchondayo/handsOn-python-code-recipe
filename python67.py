# 後続の処理をスキップ
import math
l = [1,54,35,43,-1]
for x in l:
    if x < 0:
        print(f"{x}はマイナスなのでスキップします")
        continue
        # ここ以降はスキップ
    s = math.sqrt(x)
    print(s)