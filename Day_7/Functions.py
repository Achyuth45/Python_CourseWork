def student_data(info):
    print(f"Name: {info[0]}")
    print(f"Course: {info[1]}")
    print(f"Gra Year: {info[2]}")


data= [["Achyuth","PFS","2026"],
       ["Karthikeya","PFS","2026"],
       ["sathvik","PFS","2025"],
       ["sandeep","PFS","2025"]]
for i in data:
    student_data(i)
    print("\n"*3)