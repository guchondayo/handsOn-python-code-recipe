def div_name(a,b):
    try:
        val= a / b
        print(val)
    except Exception as e:
        print("例外が発生しました")
        raise e
    div_name(7,0)
    