def get_todos():
    with open('todos_opt3.txt', 'r') as file:
        todos = file.readlines()
    return todos

while True:
    user_action = input("Type add ,show ,edit , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo+'\n')

        with open('todos_opt3.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):

        with open('todos_opt3.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        print(f"Total Works todo:{index + 1} ")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos_opt3.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:")
            todos[number] = f"{new_todo}\n"

            with open('todos_opt3.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid.")
            # user_action = input("Type add ,show ,edit , complete or exit: ")
            # user_action = user_action.strip()
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            with open('todos_opt3.txt', 'r') as file:
                todos = file.readlines()

            completed_task = todos[index].strip('\n')
            todos.pop(index)

            with open('todos_opt3.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {completed_task} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item of that number!")
            continue

    elif user_action.startswith('exit'):
        break

print("Bye!")
