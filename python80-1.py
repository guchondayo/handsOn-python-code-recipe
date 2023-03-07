# 内側の関数の実行結果をセーブしたい時どうするか
# ⇨クロージャー

def first():
    print('犯人は誰だ？')
    def second():
    #    ここのリターンの値を保持して、外で使いたい！
       return '犯人は俺だ！' 
    return second
x = first()
# xは関数そのものなので、実行してあげないとね
print(x())

