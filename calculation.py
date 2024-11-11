def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiple(x,y):
    return x*y

def division(x,y):
    return x/y

print('select operation')
print('1.Add')
print('2.subtract')
print('3.multiple')
print('4.division')

while True:
    choice = input('Enter choice(1/2/3/4):')
    if choice in('1','2','3','4'):
        try:
            n1 = float(input('Enter first number:'))
            n2 = float(input('Enter second number:'))

        except ValueError:
            print('Invalid input.please enter the number.')
            continue
        if choice == '1':
            print(n1,'+',n2, '=',add(n1,n2))

        elif choice == '2':
            print(n1,'-',n2, '=',subtract(n1,n2))

        elif choice == '3':
            print(n1,'*',n2, '=',multiple(n1,n2))

        elif choice == '4':
            print(n1,'/',n2,'=',division(n1,n2))

        next_calculation = input("let's can do next calculation?(yes/no)")
        if next_calculation == 'no':
            break
    else:
        print('invalid input')
        print('Thank you')

        
