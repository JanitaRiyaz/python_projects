import random

def winGame(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='r':
        if you=='p':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return False
        elif you=='p':
            return True
print('computer turns: Rock(r), paper(p), sessior(s) ?')
randNo= random.randint(1,3)

if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='s'


you=input('your turns: Rock(r), paper(p), sessior(s) ?')

print(f'Computer choose {comp}')
print(f'you choose {you}')
a=winGame(comp,you)  
if a==None:
    print('The match is tie!')
elif a:
    print('you won')
else:
    print('you lost')

