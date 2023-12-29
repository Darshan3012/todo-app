
while True:
    user_action = input("Type add ,show ,edit , complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            # file = open('todos.txt','r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt','r') as file:
                todos = file.readlines()
            todos.append(todo)
            # file = open('todos.txt','w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'show' | 'display':
            # file = open('todos.txt','r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt','r') as file:
                todos = file.readlines()
            # new_todos = []
            # for i in todos:
            #     item =i.removesuffix("\n")
            #     new_todos.append(item)

            # for items in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
            print(f"Total Works todo:{index+1} ")

        case 'edit':
            # file = open('todos.txt','r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt','r') as file:
                todos = file.readlines()

            # for index, item in enumerate(todos): #this is used when basic file opening and closing method is used
            #     todos[index] = item
            number = int(input("Number an todo to edit:"))
            number = number - 1
            new_todo= input("Enter new todo:")
            todos[number] = f"{new_todo}\n"
            print(todos)
            # file = open('todos.txt','w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            with open('todos.txt','r') as file:
                todos = file.readlines()

            number = int(input("Enter the number of the task completed"))
            index = number -1
            completed_task = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)
            message = f"Todo {completed_task} was removed from the list."
            print(message)
        case 'exit':
            break
        case whatever:
            print("Hey , you entered an unknown command")
print("Bye!")