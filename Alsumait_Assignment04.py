# Assignment 04 To Do list

def main():
    tasks = []
    while True:
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("0. Quit Program")
        
        user_selection = int(input("Please enter a option from the menu above: "))
        
        if user_selection == 0:
            break
        elif user_selection == 1:
            pass
        elif user_selection == 2:
            pass
        elif user_selection == 3:
            pass
        elif user_selection == 4:
            pass
    
def add_tasks(tasks):
    question = input("Would you like to add tasks? ")
    if question == "yes":
        adding = input("Enter your tasks: ")
        tasks.append(adding)
    return list(tasks)
        
def view_tasks(tasks):
    question = input("Would you like to view your tasks? ")
    if question == "yes":
        print(tasks)
        #for task in tasks:
         #   print(f"Your tasks are: {task}")
    return tasks


            

    




        
       
     
        
        
        
     


  
        

        
main()
               

    

