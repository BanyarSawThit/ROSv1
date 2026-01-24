#cart/services
from decimal import Decimal


def get_cart(session):
    return session.setdefault('cart', {})


# service each item names, price, qty, subtotal, total
def cart_summary(session):
    cart = get_cart(session)
    items = []
    total = Decimal("0.00")

    for x in cart:
        price = Decimal(cart[x]['price'])
        qty = cart[x]['quantity']
        subtotal = price * qty
        total += subtotal

        items.append({
            'id': cart[x]['id'],
            'name': cart[x]['name'],
            'price': cart[x]['price'],
            'quantity': qty,
            'subtotal': str(subtotal)
        })

    summary = {'items': items, 'total': total}

    return summary


# add +1 to the item quantity
def add_item_to_cart(session, item):
    cart = get_cart(session)
    item_id = str(item.id)
    item_price = str(item.price)

    if item_id not in cart:
        cart[item_id] = {
            'id' : item_id,
            'name': item.name,
            'price': item_price,
            'quantity': 1,
        }
    else:
        cart[item_id]['quantity'] += 1

    session.modified = True


# modify an item qty from the session cart
def update_item_quantity(session, item_id, quantity):
    cart = get_cart(session)
    item_id_str = str(item_id)
    item = cart.get(item_id_str)
    if not item:
        return

    if quantity <= 0:
        del cart[item_id_str]
    else:
        item['quantity'] = quantity

    session.modified = True


def remove_item_from_cart(session, item_id):
    cart = get_cart(session)
    item_id_str = str(item_id)
    item = cart.get(item_id_str)

    if not item:
        return
    del cart[item_id_str]

    session.modified = True


def delete_cart(session):
    session.pop('cart', None)
    session.modified = True