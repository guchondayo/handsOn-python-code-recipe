# デコレーターを使うと、高階関数が楽に書けるらしい
# ①まずは普通に書いてみる
# def add_messeage(f):
#     def new_func():
#         print("処理を開始します")
#         f()
#         print("処理を終了します")
#     return new_func

# def sample_func():
#     print("sample_funcの処理を実行します")
# decolated_func = add_messeage(sample_func)
# decolated_func()
# 結果
# ②まずは普通に書いてみる
# 処理を開始します
# sample_funcの処理を実行します
# 処理を終了します

uto = 100
def add_messeage(f):
    def new_func():
        print("処理を開始します")
        f()
        print("処理を終了します")
    return new_func
@add_messeage
def sample_func():
    print("sample_funcの処理を実行します")
sample_func()


# デコレータはどうやって判断するのかというと
# ＊＊＊＊直後の関数を引数とする＊＊＊＊＊
# @add_messeage
# def sample_func():
#     print("sample_funcの処理を実行します")
# sample_func()

# 直後
# Traceback (most recent call last):
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python81-2.py", line 26, in <module>
#     add_messeage()
# TypeError: add_messeage() missing 1 required positional argument: 'f'
# taniguchiyuujin@MacBook-Air-6 test % 