#!/c/Users/maham/AppData/Local/Microsoft/WindowsApps/python
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 12, 0, 1)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
