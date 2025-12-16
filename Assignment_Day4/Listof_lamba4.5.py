conversions = [
    lambda t: t * 1000,           #tons to kg
    lambda kg: kg * 1000,         #kg to gm
    lambda g: g * 1000,           #gm to mg
    lambda mg: mg * 0.00000220462 #milligrams to pounds       
]

tons = float(input("Enter weight in tons: "))

kg = conversions[0](tons) #tons to kg
gm = conversions[1](kg)   #kg to gm
mg = conversions[2](gm)   #gm to mg
lbs = conversions[3](mg)  #mg to lbs

print("Kilograms:", kg)
print("Grams:", gm)
print("Milligrams:", mg)
print("Pounds:",lbs)