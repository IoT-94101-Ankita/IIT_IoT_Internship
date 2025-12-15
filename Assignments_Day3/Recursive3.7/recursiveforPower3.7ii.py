def power(base, exp):
    if exp == 0:         
        return 1
    else:
        return base * power(base, exp - 1)

print("2 power 4:", power(2, 4))
