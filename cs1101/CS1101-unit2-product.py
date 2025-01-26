def product_price(list):
    set_input = set(list)
    allow_item = {1,2,3}
    item_price = {1:200.0, 2:400.00, 3:600.0}
    if allow_item >= set_input:
        price = 0
        if len(set_input) == 3:
            price = sum(item_price.values()) * 0.75
        elif len(set_input) == 2:
            for i in range(2):
                price += item_price[set_input.pop()] * 0.9
        elif len(set_input) == 1:
            price = item_price[set_input.pop()]
        print(str(price))
    else:
        print("error")