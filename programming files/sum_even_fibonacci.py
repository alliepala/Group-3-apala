# This is a file that declares ints a and b 
a, b = 0, 1

# initialize sum_even to add all the even fibonacci values
sum_even = 0

# if the value is less that 4000000 and is even, add the values to sum_even
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a+b


print(sum_even)

# answer should be 4613732
