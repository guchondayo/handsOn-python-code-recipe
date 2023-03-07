# JSと記述方法が同じですが
# 引数なしでもあらかじめ予約しておいた値を入れることができる


def func(tani=165,megu=153):
    return tani + megu

x = func()

print(x)