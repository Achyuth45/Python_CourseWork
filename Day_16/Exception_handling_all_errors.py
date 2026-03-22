try:
    a="hgh"
    b=10
    print(a+b)

except (TypeError,IndexError,TypeError,KeyError,ZeroDivisionError):
    print("error occured")

except Exception:
    print("e")
finally:
    print("end of the block")






