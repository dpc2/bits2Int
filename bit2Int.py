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


print("\nThe largest number we can represent with a signed " + str(bits) + " bit integer is:")
print(signedTotal)
print()

print("The largest number we can represent with an unsigned " + str(bits) + " bit integer is:")
print(unsignedTotal)
print()



counter = bits - 1
string1 = ''

while counter >= 0:
	string1 += '2^' + str(counter)
	if counter != 0:
		string1 += ' + '
	counter -= 1

print(string1)


counter = bits - 1
string2 = ''

while counter >= 0:
        string2 += str(2 ** counter)
        if counter != 0:
                string2 += ' + '
        counter -= 1

print(string2)
