# Assignment 04 To Do list

def main():
    tasks = []
    while True:
        print("Menu")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("0. Quit Program")
        
        user_selection = int(input("Please enter a option from the menu above: "))
        
        if user_selection == 0:
            break
        elif user_selection == 1:
            add_task(tasks)
        elif user_selection == 2:
            view_tasks(tasks)
        elif user_selection == 3:
            pass
        elif user_selection == 4:
            pass
    
def add_task(tasks):
    new_task = input("Enter the task: ")
    tasks.append([new_task, "Incomplete"])
        
def view_tasks(tasks):
    for i in range(len(tasks)):
        index = i + 1
        print(f"{index}. {tasks[i]}")
        
    print()


            

    




        
       
     
        
        
        
     


  
        

        
main()
               

    

