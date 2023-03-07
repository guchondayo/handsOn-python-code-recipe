
# いれかえるときはシンプルにかっこは入りそうもないね
address = ["神奈川県","相模原市","南区"]

pref,city,area = address

print(pref,city,area)

pref,city,area = city,area,pref

print(pref,city,area)







# JSですごいのは
# 配列を代入するときは[]=[]にせなあかんのに
# 入れ替えるだけは,だけでよろし

# let address = ["神奈川県","相模原市","南区"]

# let [pref,city,area] = address

# console.log(pref,city,area)

# pref,city,area = city,area,pref

# console.log(pref,city,area)