from .model import OrderBook


def deserializer():
    orders = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()
            if data[1] == "I":
                order = OrderBook(int(data[0]), data[1], int(
                    data[2]), float(data[3]))
                orders.append(order)
            if data[1] == "E":
                order = OrderBook(int(data[0]), data[1], int(
                    data[2]))
                orders.append(order)
    return orders
