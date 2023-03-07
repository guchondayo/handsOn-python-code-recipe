# 関数を呼ぶ前に条件付けすることが大事
def call():
    print("呼ばれちまったmyLevolution")

call()

def korehayobaren():
     print("俺を呼ばんと呼ばせんぜ")
if __name__ == "python109":
     korehayobaren()
    
# (python8) taniguchiyuujin@MacBook-Air-6 test % python python109-main.py
# 呼ばれちまったmyLevolution
# 俺を呼ばんと呼ばせんぜ
# (python8) taniguchiyuujin@MacBook-Air-6 test % python python109.py     
# 呼ばれちまったmyLevolution