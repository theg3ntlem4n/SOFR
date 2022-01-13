
def product(term):
    
    value = 1

    while term != 0:
        
        temp = (1+(0.05 * term) / 360)

        value = value * temp

        term -= 1

    return value

term = 30

cme = (product(21) - 1)

print(cme)
