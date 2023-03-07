def call(num,dev):
    try:num /dev
    except ZeroDivisionError as e:
        # eの中身はdivision by zero
        print(e)
    else: print("呂りが無事完了しました")
    finally:
        print("処理が完了しました")

call(100,0)
