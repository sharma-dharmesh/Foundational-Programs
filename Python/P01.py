"""Demonstrate how to convert from one number type to another"""

# convert to int
print(int(3.14)) # from float to int
print(int('345')) # from numeric string to int

print(int('1011',2)) # from binary to decimal int
print(int('341', 8)) # from octal to decimal int
print(int('21', 16)) # from hex to decimal int

# convert to float
print(float(35)) # from int to float
print(float('1.35')) # from numeric string to float

# convert to complex
print(complex(24)) # from int to complex with 0 as imaginary part
print(complex(23,1.1)) # from int to complex with imaginary part

# convert to bool
print(bool(35)) # from int to bool
print(bool(1.2)) # from float to bool
print(int(True)) # from bool to int
print(int(False)) # from bool to int
