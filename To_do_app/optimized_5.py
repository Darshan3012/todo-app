# from optimized_5_functions import get_todos, write_todos

import optimized_5_functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"Now:{now}")

while True:
    user_action = input("Type add ,show ,edit , complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = optimized_5_functions.get_todos()
        todos.append(todo + '\n')

        optimized_5_functions.write_todos(todos)
    elif user_action.startswith('show'):

        todos = optimized_5_functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        print(f"Total Works todo:{index + 1} ")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = optimized_5_functions.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = f"{new_todo}\n"

            optimized_5_functions.write_todos(todos)
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

            todos = optimized_5_functions.get_todos()

            completed_task = todos[index].strip('\n')
            todos.pop(index)

            optimized_5_functions.write_todos(todos)
            message = f"Todo {completed_task} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item of that number!")
            continue

    elif user_action.startswith('exit'):
        break

print("Bye!")
