a = 0
def Call(num,st):
    try:
        x = num / st
        print(x)
    except TypeError:
        print("やばいよやばいよ")
    except ZeroDivisionError:
        print("0で割ってどうすんねん")
    else:
        print("xは正常に完了いたしました")
    finally:
        print("チェック完了")
    
    Call(100,20)


