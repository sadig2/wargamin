from app.deserializer import deserializer

if __name__ == "__main__":
    orders = deserializer()
    current = []
    changed = []
    max_prices = []
    price = 0
    for order in orders:
        if order.type == "I":
            current.append(order)
        if order.type == "E":
            for cur in current:
                if cur.id == order.id:
                    current.remove(cur)
        m_price = max(
            [order.price for order in current if order.price], default=0)

        if price != m_price:
            changed.append(order)
            max_prices.append(m_price)
            price = m_price

    delimiter = 0
    mult = 0
    for i in range(len(changed)-1):
        delimiter += changed[i+1].timestamp - changed[i].timestamp
    for i in range(len(changed)-1):
        mult += (changed[i+1].timestamp - changed[i].timestamp)*max_prices[i]
    print(mult/delimiter)
