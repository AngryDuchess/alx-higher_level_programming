#!/c/Users/maham/AppData/Local/Microsoft/WindowsApps/python
print_square = __import__('4-print_square').print_square

print_square(None)
print("")

print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
