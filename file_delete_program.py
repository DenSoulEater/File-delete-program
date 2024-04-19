path = input("Write location of your file: ")
def function_file():
    os.remove(path)
def function_dir():
    os.rmdir(path)
def function_full():
    shutil.rmtree(path)
try:
    if os.path.isdir(path):
        function_dir()
        print(path + " was deleted")
    if os.path.isfile():
        function_file()
        print(path + " was deleted")
except OSError:
    rmmdir = input("Your directory is not empty, would you like to delete it with all files? (Y/N) ")
    if rmmdir.upper() == 'Y':
        function_full()
        print(path+" was deleted")
    elif rmmdir.upper() == 'N':
        print("You declined")
except TypeError:
    print("File is missing")