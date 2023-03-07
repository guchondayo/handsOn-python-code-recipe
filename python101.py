def sum_abs(x,y):
    # 2つの数の絶対値の和を求める（バグあり）
    val = abs(x) + y
    assert val >= 0
    # ここはこう想定されるよ、違ったら容赦なくエラーで返すからな！
    # ifはTRUEFALSEで返すだけだし、エラーだったら止まってくれるから
    # 間違ったまま動くのが一番やばいから→大事な前提条件！
    return val

val1 = sum_abs(-200,100)
print(val1)
# val2 = sum_abs(100,-200)
# print(val2)

# taniguchiyuujin@MacBook-Air-6 test % python python101.py
# 300
# Traceback (most recent call last):
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python101.py", line 9, in <module>
#     val2 = sum_abs(100,-200)
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python101.py", line 4, in sum_abs
#     assert val >= 0


# 以下のようにコメントアウトすると普通に動くよ
# val2 = sum_abs(100,-200)
# print(val2)

# taniguchiyuujin@MacBook-Air-6 test % python python101.py
# 300
# taniguchiyuujin@MacBook-Air-6 test % 