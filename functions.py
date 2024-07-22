import time

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a
    list of todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of todo items in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


print("Hello")

if __name__ == "__main__":
    print(get_todos())
