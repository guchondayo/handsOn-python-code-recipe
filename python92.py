# 変数の型を調べる方法
# ①type
# ②isinstance(変数,型)

x = 100
print(type(x))
print(isinstance(x,int))
print(isinstance(x,str))
l = [1,2,3]
print(type(l))

text = "abc"
print(type(text))

class Sample:
    pass
s = Sample()
print(type(s))
