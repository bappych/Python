
todos = []

while True:
    todo = input("Enter your choice: \n")
    if todo == 'add':
        todo = input("Enter an item: ")
        todos.append(todo)
    elif 'show' == todo:
        print(todos)
