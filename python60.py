goko = ["ア","イ","ウ","エ","オ"]
sanko = ["あ","い","う"]
yonko = ["ア","イ","ウ","エ"]

for a,b,c in zip(goko,sanko,yonko):
    print(a,b,c)

# Q 要素少ないときはどうするの？
# A 一番少ないものに合わせる