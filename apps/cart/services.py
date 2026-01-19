#cart/services.py
def get_cart(session):
    return session.setdefault("cart", {})

def add_to_cart(session, item):
    cart = get_cart(session)
    item_id = str(item.id)
    item_price = str(item.price)

    if item_id not in cart:
        cart[item_id] = {
            "name": item.name,
            "price": item_price,
            "quantity": 1
        }
    else:
        cart[item_id]["quantity"] +=1

    session.modified = True