def calculate_cart_total(contents):
    count = set(contents)
    disc = 0
    summ = 0
    res = []
    while (len(contents) > 0):
        for el in count:
            if el in contents and el not in res:
                contents.remove(el)
                res.append(el)
                continue
        if len(res) == 1:
            disc = 0
        if len(res) == 2:
            disc = 0.05
        if len(res) == 3:
            disc = 0.1
        if len(res) == 4:
            disc = 0.2
        summ += 10 * len(res) - (10 * len(res) * disc)
        res = []
        count = set(contents)
    return summ