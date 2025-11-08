class Tracker():
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def save_to_file(self):
        with open('data.txt', 'w') as f:
            thing = str(self._count)
            f.write(thing)

    def __str__(self):
        return f"Current count: {self._count}\n"
    
    #
    def print_content(self):
        with open('data.txt', 'r') as f:
            file_content = f.read()
            print(file_content)


