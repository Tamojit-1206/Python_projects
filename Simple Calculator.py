def Add():
    c=0
    while True:
        a=int(input('Enter the no you want to Add :'))
        c=c+a
        ch=int(input('Enter 1 to add another no 2 to exit the program and print the sum'))
        if ch==2: 
            break
    print('sum of the numbers:\n',c)
def Sub():
    a=int(input('Enter the first no you want to enter :'))
    b=int(input('Enter the second no you want to enter :'))
    if a>b:
        c=a-b
    else:
        c=b-a
    print('The Substracted value from the bigger no:\n',c)
def Divide():
    a=int(input('Enter the Neumerator :'))
    b=int(input('Enter the Denominator :'))
    c= a/b
    print('The value divided and the ans is:\n',c)
def Multiplication():
    pro=1
    while True:
        a=int(input('Enter the no you want to Multiply :'))
        pro=pro*a
        ch=int(input('Enter 1 to Multiply another no 2 to exit the program and print the product'))
        if ch==2:
            break
    print('The Product of the Nos are :\n',pro)
ask=int(input('Enter 1 for Addition \n Enter 2 for Substraction \n Enter 3 for Multiplicatoin \n Enter 4 for Divition \n Enter Choice:'))
if ask==1:
    Add()
elif ask==2:
    Sub()
elif ask==3:
    Multiplication()
elif ask ==4:
    Divide()
else:
    print('Invalid Choice !!!!!!!')