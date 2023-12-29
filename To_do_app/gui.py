import optimized_5_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window("My To-DO App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = optimized_5_functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            optimized_5_functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break


window.close()
