class GeneratorClass:
    def __init__(self, max):
        self.max = max

    def generate(self):
        count = 1
        while count <= self.max:
            yield count  # Yield the current value of count
            count += 1

    def __iter__(self):
        # This makes the class iterable by returning the generator
        return self.generate()


# Create an instance of the GeneratorClass
gen_class = GeneratorClass(5)

# Iterate through the GeneratorClass instance using a for loop
for number in gen_class:
    print(number)
