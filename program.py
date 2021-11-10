import sys

from app.serializer import deserializer

if __name__ == "__main__":
    added, deleted = deserializer()
    flags = sys.argv
    if "max" in flags:
        print("will run different script")
    if "max_price" in flags:
        prices = [order.price for order in added]
        print(max(prices))
