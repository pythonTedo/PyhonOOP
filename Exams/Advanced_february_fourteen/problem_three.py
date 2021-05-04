def stock_availability(invenory, action, *args):

    if action == "delivery":
        for el in args:
            invenory.append(el)
    if action == "sell":
        if not args:
            invenory.pop(0)
        elif isinstance(args[0], int):
            for i in range(args[0]):
                invenory.pop(0)


        else:
            invenory = [el for el in invenory if el not in args]

    return invenory

stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"), ['choco', 'vanilla', 'banana', 'caramel', 'berry']
stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"), ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
stock_availability(["chocolate", "vanilla", "banana"], "sell"), ['vanilla', 'banana']
stock_availability(["chocolate", "vanilla", "banana"], "sell", 3), []
stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"), ['banana']
stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"), ['cookie', 'banana']
stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"), ['chocolate', 'vanilla', 'banana']

