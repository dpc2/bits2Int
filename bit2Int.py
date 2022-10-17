# This script calculates max values for signed and unsigned integers


signedTotal = 0
unsignedTotal = 0
bits = input("How many bits?\n")
bits = int(bits)
x = 0

for i in range(0, bits-1):
    x = 2 ** i
    signedTotal = x + signedTotal

for i in range(0, bits):
    x = 0
    x =  2 ** i
    unsignedTotal = x + unsignedTotal


print("\nThe largest number we can represent with a signed ", end='')
print(bits, end='')
print(" bit integer is:")
print(signedTotal)
print("")

print("The largest number we can represent with an unsigned ", end='')
print(bits, end='')
print(" bit integer is:")
print(unsignedTotal)

