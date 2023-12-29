def get_todos(filepath="todos_opt3.txt"):
    """Read a text file and return the list
    of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        """
        Write the to-do items list into file.
        """
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filepath="todos_opt3.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add ,show ,edit , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        print(f"Total Works todo:{index + 1} ")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = f"{new_todo}\n"

            write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            # user_action = input("Type add ,show ,edit , complete or exit: ")
            # user_action = user_action.strip()
            continue
        except IndexError:
            print("Enter valid index!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos()

            completed_task = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)
            message = f"Todo {completed_task} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item of that number!")
            continue

    elif user_action.startswith('exit'):
        break

print("Bye!")
