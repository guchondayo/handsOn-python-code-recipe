class Sample():
    def __init__(self,x,y):
        self.x = x
        self.y = y
s = Sample(1,2)
print(dir(s))

print(hasattr(s,'x'))

# ①dir(変数)
# ②hasattr(変数,"属性の文字列")