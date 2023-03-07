# 大事　クラスの書き方
# __init__で初期化する
# ①class内で使えるselfをまず登録する__init__は、作成された段階で実行する 引数selfを忘れない
# ②selfを引数にして関数を実行できたりする
# ③名前は.nameみたいな感じで実行
class User:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    
    def throwBall(self):
        print(f"{self.name}さんの球速は平均で{self.speed}kmくらいでます")
    

otani = User("大谷",155)

otani.throwBall()

# 例えば引数名とselfの名前は異なってもOK
# アクセスされるのは、self.以降の名前
# class内で計算したりすることもできる。init内で変数を宣言し、関数内でフツーに計算して、ふつーに代入してあげれば良い

class Pref:
    def __init__(self,name,population,mult):
        self.prefname = name
        self.totalpopulation = population
        self.mult = mult
        self.result = 0
    def calc(self):
        self.result = self.totalpopulation * self.mult
        print(f"{self.prefname}の人口は{self.result}くらいになる")

kanagawa = Pref("神奈川県",200,2)
print(kanagawa.result)
# 計算する前
kanagawa.calc()
print(kanagawa.result)
# 計算した後

print(kanagawa.totalpopulation)