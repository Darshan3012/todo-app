todos = []

while True:
    user_action = input("Type add ,show ,edit , complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            # print(todos)
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            print(f"Total Works todo:{index+1} ")
        case 'edit':
            number = int(input("Number od todo to edit:"))
            number = number - 1
            todos[number] = input("Enter new todo:")
        case 'complete':
            done = int(input("Enter the number of the task completed"))
            completed_task = todos[done - 1]
            todos.remove(completed_task)
        case 'exit':
            break
        case whatever:
            print("Hey , you entered an unknown command")
print("Bye!")

# while True:
#     country = input("Type India,USA,Germany:")
#     country = country.strip()
#     match country:
#         case 'India':
#             print("Namaste")
#         case 'USA':
#             print("Hello")
#         case 'Germany':
#             print("Hallo")
#         case 'exit':
#             break
