filename = "TodoList.txt"

print("Hello User!")
print("Welcome to the ToDo List App!")
print("Would you like to create a New List, today?")

userAnswer = input("Please Respond Either YES or NO")

def todo():
    if userAnswer == 'yes' or userAnswer == 'Yes':
        print("Great. Lets get started.")
        f = open("TodoList.txt")
        f.close()
    elif userAnswer == 'No' or userAnswer == 'no':
        print("No Problem. Would you like to access your old list to Read and/or Ammend or would you like to Exit?   ")
        oldlist_input = input ("Please Respond READ to Read your Old List or EXIT to leave the application    ")
        if oldlist_input == 'Read' or oldlist_input == 'read':
            f = open("TodoList.txt", "r")
            print("Here is the List: ")
            print(f.read())
            print("Thanks for Reading! Goodbye!")
        else:
            print("Goodbye!")
    else: 
        print("That was unreadable. Please restart and make sure to respond using the set parameters..")

todo()

print("time to begin your to do list!")
f = open("TodoList.txt","r")
f.close()

def todoApp():
        f = open("TodoList.txt","a")
        todoAction = input("Please enter the item you need to action:      ")
        f.write(todoAction)
        f.write("\n")
        todoDeadline = input("Please enter the deadline for that specific Task:       ")
        f.write(todoDeadline)
        f.write("\n")

todoApp()

moreToDo = input("Would you like to add another Task to your List?")


while moreToDo == 'yes' or moreToDo == 'Yes':
    todoApp()
    moreToDo = input("Would you like to add another Task to your List?")

print("Goodbye! You can access your list if you restart the application and request to READ")




