import random
passw=int(input('Enter the length of the Password: \n'))
st=''
cha=''
spe=''
sal=''
password=''
for i in range (passw):
    ch=random.randint(1,4)
    if ch==1:
        k=random.randint(48,57)
        st+=chr(k)
        password+=st
        st=''
    elif ch==2:
        z=random.randint(65,90)
        cha+=chr(z)
        password+=cha
        cha=''
    elif ch==3:
        r=random.randint(35,38)
        spe+=chr(r)
        password+=spe
        spe=''
    elif ch==4:
        o=random.randint(97,122)
        sal+=chr(o)
        password+=sal
        sal=''
print('Generated Password:',password)