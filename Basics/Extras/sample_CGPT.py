class MagicNotebook:
    def __init__(self, color):
        self.color = color

    def write(self, message):
        print(f"Writing '{message}' in {self.color} notebook.")

# Creating a magic notebook with a specific color
my_notebook = MagicNotebook("blue")

# Writing something in the notebook
my_notebook.write("Hello, magic world!")

my_notebook = MagicNotebook("red")

my_notebook.write("Hi, world of magics!")