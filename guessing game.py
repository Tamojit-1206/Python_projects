import random
a=int(input('Guess a number from 0 to 9'))
c=random.randint(0,9)
if a==c:
    print('Your guess was correct, you got 1 point')
else:
    print('OOpsss!!!, Better Luck Next Time')