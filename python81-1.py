# 高階関数の使い所
# # ①内部関数が容易されている
# ②外（グローバル）での処理をカスタマイズしたい時

# 内側愛してる
# 私もorは　ここをカスタマイズ
# 嬉しい・悲しい

def Hanashi(a):
    print("愛してる")
    def Answer():
        if a() == "私も":
            return "幸せ"
        else:
            return "こんちきしよー"
    return Answer
# ここをカスタマイズしておけばいつでも切り替えられる、
def ok():
    return "私も"
def no():
    return "きしょい"
# 2個いる
print(Hanashi(ok)())