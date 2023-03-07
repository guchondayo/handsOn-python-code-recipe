# 例外の使い方
def div_num(a,b):
  try:
      val = a/b
      print(val)
  except ZeroDivisionError:
    print("ゼロで除算してるぜ")
div_num(100,0)

# インデントが結構厳しく見られるので注意すること