# file_opener_function.py

from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


# Example usage
if __name__ == "__main__":
    with open_file("example_function.txt", "w") as f:
        f.write("Hello from function-based context manager!")
