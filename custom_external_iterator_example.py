class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.iterator = CountUpToIterator(max)

    def __iter__(self):
        return self.iterator


class CountUpToIterator:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


def main():
    print("Manual iteration using iter() and next():")
    counter = CountUpTo(3)
    iterator = iter(counter)  # get the iterator object

    while True:
        try:
            value = next(iterator)  # manually get the next value
            print(value)
        except StopIteration:
            break  # stop when iteration is complete


if __name__ == "__main__":
    main()
