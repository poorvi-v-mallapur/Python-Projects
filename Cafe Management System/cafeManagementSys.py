menu = {
    'pizza' : 190,
    'donut' : 120,
    'pasta' : 150,
    'coffee' : 110,
    'pastry' : 180
}

total_price = 0

print('welcome to POORVI\'s cafe')

item1 = input('Enter the first item you would like to order: ')
if item1 in menu:
    total_price += menu[item1]
else:
    print(f'Ordered item {item1} doesnt exist in our menu')

choice = input('Would you like to order something else? (yes/no): ')
if choice == 'yes':
    item2 = input('Enter the second item you would like to order: ')
    if item2 in menu:
        total_price += menu[item2]
    else:
        print(f'Ordered item {item2} doesnt exist in our menu')

print(f'Thank you for ordering. Your bill amount is {total_price}')