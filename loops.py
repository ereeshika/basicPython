# # While Loop
# i = 1
# while i <= 5:
#     print("I love you "*i)
#     i += 1
# print("======================================")
# # Learn Do While Loop

# # For Loop

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)
# print("======================================")

# # In a range function list = range(0,1,2) 0=starting value, 1=ending value, 2=step
# # For Loop with Range
# numbers = range(1, 6, 2)
# for i in numbers:
#     print(i)
# # alternatively
# for i in range(1, 6, 2):
#     print(i)
# print range in a single line
# here sep is the separator and * is the repetition of unpacking a list
print(*range(1, 6, sep=''))

# Tuples
# Tuples are immutable.  We use square brackets to define a list and paranthesis to define a tuple
numbers = (1, 2, 3, 4, 5)
