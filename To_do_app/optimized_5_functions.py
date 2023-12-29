def get_todos(filepath="todos_opt3.txt"):
    """Read a text file and return the list
    of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filepath="todos_opt3.txt"):
    """
        Write the to-do items list into file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
print(type(__name__))
if __name__=="__main__":
    print("Hello")
    print(get_todos())