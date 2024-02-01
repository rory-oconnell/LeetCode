def simple_generator():
    yield "Hello"
    yield "World"

# Create a generator object
gen = simple_generator()

# Iterate through the generator
for value in gen:
    print(value)