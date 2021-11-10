from .model import OrderBook


def deserializer():
    orders_added = []
    orders_deleted = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()
            if data[1] == "I":
                order = OrderBook(int(data[0]), data[1], int(
                    data[2]), float(data[3]))
                orders_added.append(order)
            if data[1] == "E":
                order = OrderBook(int(data[0]), data[1], int(
                    data[2]))
                orders_deleted.append(order)
    return orders_added, orders_deleted
