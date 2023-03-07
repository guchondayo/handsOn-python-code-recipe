# 例外処理を行うにあたって、１つだけだと心許ない
def check_num(a,b):
    try:
        num = a / b
        print(num)
    except TypeError:
        print("?なんの型だこれ")
    except ZeroDivisionError:
        print("0で割ってるけど、、")
    except AttributeError:
        print("属性ねーぞ")
a = 100
b = "unko"

check_num(a,b)
a = 100
b = 0
# check_num(a.unko(),b)
check_num(a,b)

