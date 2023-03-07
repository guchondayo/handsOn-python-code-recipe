# 例外の使い方
def div_num(a,b):
  try:
      val = a/b
      print(val)
  except BaseException:
    print("何か間違っている")
div_num(100,"a")

# インデントが結構厳しく見られるので注意すること


# AttributeError 存在しない属性

def div_Att(a):
  try:
      print(a.unko())
  except AttributeError:
    print("そんな属性がないぞ")
div_Att(100)

# インデントが結構厳しく見られるので注意すること
# 例外を書かなかった場合
# Traceback (most recent call last):
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python94.py", line 20, in <module>
#     div_Att(100)
#   File "/Users/taniguchiyuujin/Desktop/handsOn/python/test/python94.py", line 17, in div_Att
#     print(a.unko())
# AttributeError: 'int' object has no attribute 'unko'
# 例外を書いた場合
# そんな属性がないぞ
# こうやることで、使っている人は

# ＊色々なエラーがあるので、細かく指摘したいのか、もしくは大雑把に表記させたいのかで、使い分けよう