def first():
    print('firstが実行された')
    def second():
        print('secondが実行された')
    second()
first()    


# インデントによって実行のタイミングがずれるようになっている
# print('firstが実行された')
# def second():
# ＊２つ目のインデントと一つ目の処理のインデントを合わせる

# 実行順
# firstが実行された
# secondが実行された