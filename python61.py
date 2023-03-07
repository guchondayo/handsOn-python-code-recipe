l = ["ア","イ","ウ","エ","オ"]
for y in reversed(l):
    print(y)

# 飛ばし飛ばしで描きたいときはこっち
for z in l[::-2]:
    print(z)