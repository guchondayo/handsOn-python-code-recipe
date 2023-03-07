def sample_generator():
    # ジェネレーター関数
    print("処理開始")
    yield 'おはよう'
    print("処理再開")
    yield 'こんにちわ'
    print("処理開始")
    yield 'こんばんわ'

gen_obj = sample_generator()
# <generator object sample_generator at 0x10abf4c80>と出るので、オブジェクトとして返される
print(gen_obj)
print(next(gen_obj))
# 全体で回すにはforで回せば良い
for x in gen_obj:
    print(x)

# まず、returnだと、returnされた瞬間に終了してしまう
# 以下みたいなものはエラー
# def sample_generator():
#     # ジェネレーター関数
#     print("処理開始")
#     return 'おはよう'
#     print("処理再開")
#     return 'こんにちわ'
#     print("処理開始")
#     return 'こんばんわ'

# メモリの節約にいいらしい
# https://qiita.com/keitakurita/items/5a31b902db6adfa45a70
