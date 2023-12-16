from shopping_cart import Cart

def test_add_to_cart():
    cart = Cart()
    cart.add_to_cart(item=[{
        "itemno": "jghg",
        "item": "Back Pack",
        "quantity": 5,
        "cost": 850
    }])
    cart.add_to_cart(item=[{
        "itemno": "jghg",
        "item": "Back Pack",
        "quantity": 5,
        "cost": 850
    }])

    cart.print_cart_items()


if __name__ == '__main__':
    test_add_to_cart()