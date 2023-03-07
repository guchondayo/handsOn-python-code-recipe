# 実行時に引数を指定したい
import sys
print(sys.argv)
print(sys.argv[0])
# どういうことかというと

# % python python102.py 1 2
# という感じで、コマンドを打った時にモジュール名の後ろに引数を加えることができる
# その引数を表示したいぜ

# taniguchiyuujin@MacBook-Air-6 test % python python102.py 1 2
# ['python102.py', '1', '2']

# 使い所