# ISBN 13 Check Digit

l = []

l1 = []

def thirteen():
    while True:
        n = input("Enter the 12 digit ISBN number: ")
        if len(n)==12 and n.isdigit():
            for digit in n:
                l.append(int(digit))
            break
        elif n=='exit':
            print("Goodbye!")
            exit()
        else:
            print("Error: Please enter a valid ISBN 12 digit number or type 'exit'.")
            
            
def ten():
    while True:
        p = input("Enter the 9 digit ISBN number: ")
        if len(p)==9 and p.isdigit():
            for digit in p:
                l1.append(int(digit))
            break
        elif p=="exit":
            print("Goodbye!")
            exit()
        else:
            print("Error: Please enter a valid ISBN 9 digit number or type 'exit'.")


def ten_calc():
    t = 0
    for i in range(len(l1)):
        t += l1[i] * (10 - i)
    
    r = t % 11
    di = 11 - r
    if di == 10:
        di= 'X'
    elif di== 11:
        di = 0

    print("ISBN check digit: ", di)
    
    
def thirteen_calc():
    a = True
    for i in range(len(l)):
        if a:
            l[i]=l[i]*1
            a = False
        else:
            l[i]=l[i]*3
            a = True

    s = sum(l)
    m = s % 10
    d = (10 - m) % 10

    print("ISBN check digit: ", d)
    
    

while True:
    cho = input("Check digit for: [1]ISBN 10 [2]ISBN 13 [3]Exit: ")
    if cho == '1':
        ten()
        ten_calc()
    elif cho == '2':
        thirteen()
        thirteen_calc()
    elif cho == '3':
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
