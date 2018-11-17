'''
Quadratic equation root calculator
'''

print('Run directly')

def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)

    print('x1: ', x1)
    print('x2: ', x2)

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    
