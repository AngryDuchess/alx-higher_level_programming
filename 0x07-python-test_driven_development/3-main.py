#!/c/Users/maham/AppData/Local/Microsoft/WindowsApps/python
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name(None)
say_my_name("24", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
