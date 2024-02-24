# Assignment 04 To Do list

def main():
    tasks = []
    add_tasks(tasks)
    view_tasks(tasks)
    mark_tasks(tasks)
    
    
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
            
def mark_tasks(tasks):
    question = input("Would you like to mark any tasks? ")
    if question == "yes":
        for index, task in tasks:
            print(f"{index}. {task}")
        mark = input("Enter the task number you would like to mark: ")
        
        tasks[mark] += "Complete"
    
    return list(tasks)




        
       
     
        
        
        
     


  
        

        
main()
               

    

