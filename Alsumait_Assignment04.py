# Assignment 04 To Do list

def main():
    tasks = []
    add_tasks(tasks)
    view_tasks(tasks)
    
def add_tasks(tasks):
    adding = input("Enter your tasks: ")
    tasks.append(adding)
    return list(tasks)
        
def view_tasks(tasks):
    for task in tasks:
        print(f"Your tasks are: {task}")
        

        
main()
               

    

