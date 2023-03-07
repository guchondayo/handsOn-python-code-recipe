# 処理をストップしたい
import time
first = 1
time.sleep(first)
print(str(first) + "秒経過")
sec = 3
time.sleep(sec)
print(str(sec) + "秒経過")

# ①処理は上から下まで順番に流れていく
# ②time.sleep(行数)→ここの秒数だけ中断するのだ

# 使い所

# 使い所があんまりわかっていない
