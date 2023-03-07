#  annotationとは
# javascriptとtypescriptとの違いみたい
# :型で記載するので、jsと変わらない

x:int = 155
y:str = "大谷"

def call(z:int,zz:str):
    return f'{zz}は{z}kmです'
print(call(x,y))

# 変数と文字列の融合
# https://note.nkmk.me/python-string-concat/