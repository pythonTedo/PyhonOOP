def flights(*kwargs):
    my_dict = {}

    temp = ""

    for x in kwargs:
        if isinstance(x, str):
            if x not in my_dict.keys():
                my_dict[x] = 0
                temp = x
            else:
                continue
        elif isinstance(x, int):
            my_dict[temp] += x


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))