products = {
    'product_1': {
        'title': 'HP',
        'price': 1000,
        'photo': '1.jpg',
        'params': {
            'diag': 15.6,
            'proc': 'Intel Core i5',
            'videoc': 'Intel HD graphics 4000',
            'memory_gig': 8
        }
    },

    'product_2': {
        'title': 'Dell Alienware',
        'price': 3000,
        'photo': '2.jpg',
        'params': {
            'diag': 15.6,
            'proc': 'Intel Core i7',
            'videoc': 'NVidia GTX 1080',
            'memory_gig': 16
        }
    },

    'product_3': {
        'title': 'Acer',
        'price': 1500,
        'photo': '3.jpg',
        'params': {
            'diag': 17,
            'proc': 'Intel Core i7',
            'videoc': 'NVidia GTX 960m',
            'memory_gig': 8
        }
    }
}

search = input('Input what you search: ')
for product in products.items():
    for items in product[1].items():
        # print(items)
        try:
            for params in items[1].items():
                # print(params)
                if params[1] == search:
                    print(product)
        except AttributeError:
            if items[1] == search:
                print(product)
