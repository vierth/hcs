# Floating point numbers are created with decimal points
1.0
1.5
1000.1

# They are not precise (note how they get progressively more wrong)
num = 0.0
for i in range(100):
    num += .01
    print(num)

# Adding integers and floats returns a float
print(1 + 1.0)

1 + 1 # addition
1 - 1 # subtraction
2 * 2 # multiplication
10/5 # divison (returns float)
10//3 # integer divison (returns integer)
10 % 3 # modulo, returns remainder
2**4 # exponential