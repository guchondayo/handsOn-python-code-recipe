import traceback

try:
    x = 1/0
except Exception as e:
    print("エラー情報¥n" + traceback.format_exc())

# taniguchiyuujin@MacBook-Air-6 test % python python100.py
# エラー情報¥nTraceback (most recent call last):
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python100.py", line 4, in <module>
#     x = 1/0
# ZeroDivisionError: division by zero