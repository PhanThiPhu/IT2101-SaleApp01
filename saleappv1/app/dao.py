def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 15',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }, {
        'id': 2,
        'name': 'Galaxy S23',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }, {
        'id': 3,
        'name': 'Samsung A22',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }, {
        'id': 4,
        'name': 'iPhone 13',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }, {
        'id': 5,
        'name': 'iPhone 14',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }, {
        'id': 6,
        'name': 'iPhone 15 Pro',
        'price': 20000000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg'
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0 ]
    return products
