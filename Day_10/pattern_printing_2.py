'''
*
**
***
****
*****
Docstring for python_programs.Python_Fullstack_course_work.pattern_printing_2
'''

n=int(input("Enter a number:"))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()

'''
    *
   **
  ***
 ****
*****
Docstring for python_programs.Python_Fullstack_course_work.pattern_printing_2
'''

n=int(input("Enter a number:"))
for row in range(n):
    for i in range(n-row-1):
        print(" ",end=" ")

    for col in range(row+1):
        print("*",end=" ")
    print()


n=int(input("Enter a number:"))
for row in range(n*2):

    if n<=5:
        print("*"*row+1,end=" ")
    else:
        print("*")

    
