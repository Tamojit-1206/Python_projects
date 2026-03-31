task=[]
while True:
    ch=int(input('Enter your choice!!! \n 1. To Add a Task \n 2. To Delete The Recent Task \n 3. To See Tasks \n 4. To Exit the Program'))
    if ch==1:
        ntask=input('Enter The Task :\n')
        task.append(ntask)
    if ch==2:
        if len(task) ==0:
            print('Under Flow!!!')
        else:
            print('Deleting the Recent Task Added!!!')
            task.pop()
    if ch==3:
        if len(task) ==0:
            print('Under Flow!!!')
        else:
            for i in task:
                print(i)
    if ch==4:
        print('Exiting......')
        break
    else:
        print('Invalid Choice!!!!!')
        break