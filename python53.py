# 大事なのは、Falseとして判定されるか否かを把握
xInt = 0
if xInt:
    print(True)
else:
    print(False)

# listとか空でもそんな感じ
xlist = []
if xlist:
    print("成功しちゃったよ")
else:
    print(False)