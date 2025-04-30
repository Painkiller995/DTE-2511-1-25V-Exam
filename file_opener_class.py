# file_opener_class.py


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# Example usage
if __name__ == "__main__":
    with FileOpener("example_class.txt", "w") as f:
        f.write("Hello from class-based context manager!")
