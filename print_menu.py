'''
Unit Converter: Miles and Kilometers
'''

print('Use the Python, not import')

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles is: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers is: {0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion wold you like to do?: ')
    if choice == '1':
        km_miles()

    elif choice == '2':
        miles_km()

    else:
        print('Choose either 1 or 2')
