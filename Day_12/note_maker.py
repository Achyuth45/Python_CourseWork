notes={}
name=input("entr your name:")
while True:
    print(f"Hey {name} welcome to the notes... `")
    if notes:
        for i in notes:
            print(i.ljust(15," "),notes[i])
    else:
        print("Empty notes")
    print("[A]dd the note")
    print("[U]pdate the note")
    print("[E]dit the note")
    print("[B]ack the note")

    action=input("Enter the action do you want to do:").upper()

    if action=="A":
        note_name=input("enter your note name:").title()
        content=input("Enter the content you want in your note:")
        notes[note_name] = content
        print(f"{note_name} : {content}")


    elif action=="U":
        note_name=input("enter your note name:").title()
        if note_name in notes:
            content=input("Enter the content you want in your note:")
            notes[note_name] = content
            print(f"{note_name} : {content}")
        else:
            print("notes is empty")


    elif action=="E":
        note_name=input("enter your note name:").title()
        if note_name in notes:
            content=input("Enter the content you want in your note:")
            notes[note_name] += content
            print(f"{note_name} : {content}")
        else:
            print("notes is empty")
    else:
        break
        print("Thank you have a nice day")




        

    