
my_holocron = [1, 2, 3]

for item in my_holocron:
    print(f"First pass: {item}")
# Output:
# First pass: 1
# First pass: 2
# First pass: 3

for item in my_holocron:
    print(f"Second pass: {item}")
# Output:
# Second pass: 1
# Second pass: 2
# Second pass: 3


########################################################################################

# A generator expression is a one-shot iterator. We will learn more about them later!
self_destructing_message = (x for x in range(3))

for item in self_destructing_message:
    print(f"Reading the message: {item}")
# Output:
# Reading the message: 0
# Reading the message: 1
# Reading the message: 2

#The message is gone. If we try to read it again, nothing happens!
for item in self_destructing_message:
    print(f"Message is gone: {item}")
# Output: (Nothing is printed!)