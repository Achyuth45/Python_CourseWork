try:
    a=20
    if a > 10:
        print("good")
except NameError:
    print(" 'a' is not defined")
else:
    print("no errors")

finally:
    print("End of the block")