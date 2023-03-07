# 複数の値を返却したいときはどうすればいいのか？

def Func():
    return 100,200

x = Func()
print(x)

# →セット型に返される

# JSだと点のケツだけ返される
# function Func(){
#  return 1,2,3
# }

# x = Func()
# console.log(x)
# →3

# 配列でもOK
# function Func(){
#  return [1,2,3]
# }

# x = Func()
# console.log(x)
# →[1, 2, 3]


# キーバリュー返せる
# function Func(){
#  return {たに:1,飲む:2,た:3}
# }
# x = Func()
# console.log(x)
# {
#   た: 3,
#   たに: 1,
#   飲む: 2
# }