import sys

from app.serializer import deserializer

if __name__ == "__main__":
    added, deleted = deserializer()
    prices = [order.price for order in added]
    timestamp_substracted = [(d.timestamp -
                             a.timestamp, a.price) for a in added for d in deleted if a.id == d.id]
    flags = sys.argv

    if "max_price" in flags:
        print(max(prices))
    if "time" in flags:
        delimiter = sum([k[0] for k in timestamp_substracted])
        multipled_list = sum([k[0]*k[1] for k in timestamp_substracted])
        awg = multipled_list/delimiter
        print(round(awg, 2))
