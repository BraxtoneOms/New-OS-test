num = 255

print("Decimal: ", num)
print("Binary: ", bin(num))
print("Hexadecimal: ", hex(num))


wgt = int(input("Weight: "))
clbs = input("(K)gs or (L)bs: ")
clbs_u = clbs.upper()

if clbs_u == "K":
    result = wgt/0.45
    print(result)
elif clbs_u == "L":
    result = wgt*0.45
    print(result)

