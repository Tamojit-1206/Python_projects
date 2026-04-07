import mysql.connector as c
h=input('Enter Host:\n')
u=input('Enter User:\n')
p=input('Enter Password:\n')
d=input('Enter Database:\n')
con=c.connect(host=h, user=u, password=p, database=d)
cursor=con.cursor()
create=int(input('Enter 1.To Create Table\n 2. To Use an existing Table\n Enter your Choice:\n'))
tname=input('Enter the Table Name You want to Create or Use:\n')
if create==1:
    table='create table {}(R_No int primary key, student_name varchar(30), class int not null, section varchar(10) not null, marks int not null)'.format(tname)
    cursor.execute(table)
    print('Table created and Using Table !!!!!')
while True:
    ch=int(input('Enter 1.To Insert Values in the Table\n 2. To Display the Table\n 3. To Search a Student using Roll No\n 4. To update data in the Table\n 5.to Delete an Entry of Student\n Enter your Choice:\n'))
    if ch==1:
        R_No=int(input('Enter Roll Number:\n'))
        student_name=input('Enter Student Name:\n')
        Class=int(input('Enter Class:\n'))
        section=input('Enter Section of the student:\n')
        marks=int(input('Enter Marks of the Student:\n'))
        quary="insert {} values({},'{}',{},'{}',{})".format(tname,R_No,student_name,Class,section,marks)
        cursor.execute(quary)
        con.commit()
    elif ch==2:
        quary="select * from {}".format(tname)
        cursor.execute(quary)
        a=cursor.fetchall()
        for i in a:
            print(i)
    elif ch==3:
        find=int(input('Enter the Roll No of the Student you want to Search:\n'))
        quary="Select * from '{}' where R_No={}".format(tname,find)
        cursor.execute(quary)
        a=cursor.fetchone()
        print(a)
    elif ch==4:
        while True:
            uch=int(input('Enter 1. To Update Student Name\n 2. To Update Class \n 3. To Update Section\n 4. To Update Marks\n 5. To Exit Updating!!! \n'))
            if uch==1:
                Rno=int(input('Enter the Roll No of the student whose Name you want to Update!!!!\n'))
                nst_n=input('Enter New Name of The Student:\n')
                quary="Update {} set student_name='{}' where R_No={}".format(tname,nst_n,Rno)
                cursor.execute(quary)
                con.commit()
            elif uch==2:
                Rno=int(input('Enter the Roll No of the student whose Name you want to Update!!!!\n'))
                nclass=int(input('Enter the New Class of The Student:\n'))
                quary="Update {} set class={} where R_No={}".format(tname,nclass,Rno)
                cursor.execute(quary)
                con.commit()
            elif uch==3:
                Rno=int(input('Enter the Roll No of the student whose Name you want to Update!!!!\n'))
                nsec=input('Enter the New Section of The Student:\n')
                quary="Update {} set section='{}' where R_No={}".format(tname,nsec,Rno)
                cursor.execute(quary)
                con.commit()
            elif uch==4:
                Rno=int(input('Enter the Roll No of the student whose Name you want to Update!!!!\n'))
                nmark=int(input('Enter the New Marks of The Student:\n'))
                quary="Update {} set marks={} where R_No={}".format(tname,nmark,Rno)
                cursor.execute(quary)
                con.commit()
            elif uch==5:
                print("Exiting Update!!")
                break
            else:
                print("Wrong Choice, Exiting Update!!")
                break
    elif ch==5:
        Rno=int(input('Enter the Roll No of the student whose Name you want to Delete!!!!\n'))
        quary="Delete from {} where R_no={}".format(tname,Rno)
        cursor.execute(quary)
        con.commit()
        print('Entry Deleted!!!')
    elif ch==6:
        print('Exiting Program!!!!!!')
        break
    else:
        print('Invalid Choice!!!!!!')
        break