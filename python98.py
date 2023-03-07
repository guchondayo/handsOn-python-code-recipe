# ＊if文と組み合わせる
# ＊例外クラスにないものを作成する

def call(num,dev):
    a = num /dev
    if num / dev == 3:
        raise "3はやめてください"
    print(a)

call(6,2)