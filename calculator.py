#calculator using WHILE-IF-ELSE-EXIT
while True:
    n1 = float(input("Enter Your First Number :  "))
    op = input("Please choose your aperator - +,-,*,/,% : ")
    n2 = float(input("Enter Your Second Number :  "))

    if op == '+':
        print(f'sum of {n1}+{n2} is {n1+n2}')
    elif op == '-':
        print(f'Difference of {n1}-{n2} is {n1-n2}')
    elif op == '*':
        print(f'product of {n1}*{n2} is {n1*n2}')
    elif op == '/':
        if n1 and n2 == 0:
            print(f'0 is not divisibe of anty Number')
        else:
            print(f'Divisible of {n1}/{n1} is {n1/n2}')
    else:
        print('invalid Entry !')
        exit()

    choice = input('Do you want to exit : y/n ')
    if choice == 'y':
        print('Great to help you')
        exit()

