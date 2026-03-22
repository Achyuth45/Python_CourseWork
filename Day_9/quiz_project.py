data = {
    1: {
        "question": "What is the output of print(type(3.14))?",
        "options": {
            "a": "<class 'int'>",
            "b": "<class 'float'>",
            "c": "<class 'str'>",
            "d": "<class 'complex'>"
        },
        "answer": "b"
    },

    2: {
        "question": "Which of the following data types is immutable?",
        "options": {
            "a": "list",
            "b": "set",
            "c": "dictionary",
            "d": "tuple"
        },
        "answer": "d"
    },

    3: {
        "question": "What will be the output of print(len(\"Python\"))?",
        "options": {
            "a": "5",
            "b": "6",
            "c": "7",
            "d": "Error"
        },
        "answer": "b"
    },

    4: {
        "question": "Which keyword is used to create a function in Python?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "create",
            "d": "func"
        },
        "answer": "b"
    },

    5: {
        "question": "What is the output of print(10 // 3)?",
        "options": {
            "a": "3.33",
            "b": "3",
            "c": "4",
            "d": "Error"
        },
        "answer": "b"
    },

    6: {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "a": "^",
            "b": "**",
            "c": "//",
            "d": "%"
        },
        "answer": "b"
    },

    7: {
        "question": "What will be the output of print(bool(0))?",
        "options": {
            "a": "True",
            "b": "False",
            "c": "0",
            "d": "Error"
        },
        "answer": "b"
    },

    8: {
        "question": "Which function is used to take input from the user?",
        "options": {
            "a": "read()",
            "b": "scan()",
            "c": "input()",
            "d": "get()"
        },
        "answer": "c"
    },

    9: {
        "question": "What is the output of print(\"Hello\"[::-1])?",
        "options": {
            "a": "Hello",
            "b": "olleH",
            "c": "H",
            "d": "Error"
        },
        "answer": "b"
    },

    10: {
        "question": "Which of the following is a valid variable name?",
        "options": {
            "a": "1value",
            "b": "value-1",
            "c": "value_1",
            "d": "value 1"
        },
        "answer": "c"
    }
}
score=0
for i in data:
    print(f"Question {i}: {data[i]['question']}")

    print("\n")


    for j, k in data[i]["options"].items():
        print(f"{j}. {k}")
    print("\n")


    user_answer=input("enter an option: ")
    if user_answer==data[i]["answer"]:
        print("Correct")
        score+=1
    else:
        print("Wrong answer")

        
print("\n")
print(f"Your total score is {score/len(data)}")
    

