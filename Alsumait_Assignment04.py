# Assignment 04 To Do list

def main():
    tasks = []
    add_tasks(tasks)
    view_tasks(tasks)
   
    
    
def add_tasks(tasks):
    question = input("Would you like to add tasks? ")
    if question == "yes":
        adding = input("Enter your tasks: ")
    tasks.append(adding)
    return list(tasks)
        
def view_tasks(tasks):
    question = input("Would you like to view your tasks? ")
    if question == "yes":
        for task in tasks:
            print(f"Your tasks are: {task}")
    return tasks


            

    print("Task deleted.")
    
    return list(tasks)




        
       
     
        
        
        
     


  
        

        
main()
               

    

