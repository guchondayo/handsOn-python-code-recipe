# デコレーターに可変長引数を使う
# デコレータに引数を加える
def add_message(f):
    def new_func(*args, **kwargs):       
        print("処理を開始します")
        result = f(*args, **kwargs)
        print("処理を終了します")
        return result
    return new_func
@add_message
def add_one(num):
    print("パラメータ:{}".format(num))
    return num + 1
result = add_one(1)
print("戻り値:{}".format(result))

# *args, **kwargsを使わなくてもいいが、add_one(num):だけじゃなく
# 色々な関数があるし、引数の数がセンサ満別だから、可変調を使った方がいいってこと
# https://blog.pyq.jp/entry/Python_kaiketsu_200421

#     def new_func(num):       
#         print("処理を開始します")
#         result = f(num)
#         print("処理を終了します")
#         return result
#     return new_func
# @add_message
# def add_one(num):
#     print("パラメータ:{}".format(num))
#     return num + 1
# result = add_one(1)
# print("戻り値:{}".format(result))
