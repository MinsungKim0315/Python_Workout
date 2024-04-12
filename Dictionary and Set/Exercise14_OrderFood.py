MENU = {'sandwich': 10, 'tea':7, 'salad':9}

def restaurant():
    total = 0
    while True:
        order = input('Order: ')
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} costs {MENU[order]}, total is {total}')
        if not order:
            break
        if order not in MENU:
            print(f'Sorry, we are fresh out of {order} today.')
            continue
    print(f'your total is {total}')

restaurant()