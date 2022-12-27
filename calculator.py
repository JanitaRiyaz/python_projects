def sum(a,b):
    answer=a+b
    print(f"{a} + {b} = {answer}")

def minus(a,b):
    answer=a-b
    print(f"{a} - {b} = {answer}")
def mul(a,b):
    answer=a*b
    print(f"{a}  * {b} = {answer}")
def div(a,b):
    answer=a/b
    print(f"{a}  / {b} = {answer}")

while True:

 print("A. Addition")
 print("B. Substraction")
 print("C. Multiplication")
 print("D. Division")

 choice=input('Enter your choice: ')

 if choice=='a' or choice=='A':
    print('Addition')
    a=int(input('Enter a number: '))
    b=int(input('Enter second number: '))
    sum(a,b)


 elif choice=='b' or choice=='B':
    print('Substraction')
    a=int(input('Enter a number: '))
    b=int(input('Enter second number: '))
    minus(a,b)

 elif choice=='c' or choice=='C':
    print('Multiplication')
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    mul(a,b)

 elif choice=='d' or choice=='d':
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    div(a,b)
    quit()



