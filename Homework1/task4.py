def cacluate_discount(cost, discount):
    total = cost - (cost*(discount/100))
    print(total)
    return total
cacluate_discount(10, 10)
assert cacluate_discount(10, 10) == 9
