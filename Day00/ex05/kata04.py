import decimal

kata = (0, 4, 132.42222, 10000, 12345.67)


print("module_%02d, ex%02d : %.2f," % (kata[0], kata[1], kata[2]), end="")
print(" %.2E, %.2E" % (decimal.Decimal(kata[3]), decimal.Decimal(kata[4])))
