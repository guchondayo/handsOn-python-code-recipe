s1 = {1,2,4,6}
s2 = {9,3,4,6}

# setはこうなってしまうんですよ、、
# ss = s1 + s2
# print(ss)
# taniguchiyuujin@MacBook-Air-6 test % python python44.py         
# Traceback (most recent call last):
#   File "/Users/taniguchiyuujin/Desktop/ハンズオン/python/test/python44.py", line 4, in <module>
#     ss = s1 + s2
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# tanigu(chiyuujin@MacBook-Air-6 test % 

# s3にs1とs2をがっち
s3 = s1.union(s2)
print(s3)
