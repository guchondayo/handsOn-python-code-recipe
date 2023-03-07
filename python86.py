# Userを継承したStuden tを作る方法
class User:
    def __init__(self,name,pref):
        self.name = name
        self.pref = pref
    def introduce(self):
        print(f"{self.name}さん{self.pref}出身です")

tani = User("谷口","神奈川県")
tani.introduce()
    
class studentUser(User):
    def __init__(self, name, pref,japanese,math):
        super().__init__(name, pref)
        self.japanese = japanese
        self.math = math
    def answer_question(self,desc):
        print(f"{self.name}さんの国語の成績は{self.japanese}店です{desc}です")
        print(f"{self.name}さんの国語の成績は{self.math}店です{desc}です")

uto = studentUser("谷家ん","神奈川県",45,50)
uto.answer_question("優秀")

# ①普通のクラス→クラス名横の（）がない　継承先（）の中に継承元
# ②def __init__(self,name,pref):第一引数はselfそ例外は使いたい引数。継承したときの右側が引数
# ③uto.answer_question("優秀")大に引数以降はこんな感じで追加することもできる