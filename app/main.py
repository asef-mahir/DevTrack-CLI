from app.database import init_db
from app.services import task_service
from rich.console import Console
console = Console()

def main():
    init_db.initialize_database()
    
    while True:
        console.print("[bold green] Welcome to your personal Task Manager [/bold green]")
        console.print("[bold magenta] -------------- DevTack -------------- [/bold magenta]")
        print("\n")

        console.print("[bold yellow] 1. Add a Task [/bold yellow]")
        console.print("[bold yellow] 2. Show List of All Tasks [/bold yellow]")
        console.print("[bold yellow] 3. Complete a Task [/bold yellow]")
        console.print("[bold yellow] 4. Delete a Task [/bold yellow]")
        console.print("[bold yellow] 5. Exit [/bold yellow]")

        try: 
            console.print("[bold yellow] Choose an option: [/bold yellow]")
            user_inp = int(input()) 
        except ValueError as e:
            console.print("[bold red] Try again with a valid digit between 1 to 5 [/bold red]")
            continue 

        if user_inp == 1:
            console.print("[bold green] Enter Task Name: [/bold green]")
            task_title = input()
            new_task_id = task_service.add_task(task_title)
            if new_task_id: 
                console.print(f"[bold cyan] New task added with task id : {new_task_id} [/bold cyan]")
            else:
                console.print("[bold red] Invalid title [/bold red]")
    
        elif user_inp == 2:
            console.print("[bold green] Displaying the list of the tasks: \n [/bold green]")
            task_list = task_service.list_tasks()
            for task in task_list:
                task_id, title, status, created_at, completed_at = task 
                console.print(f"[bold cyan] {task_id}. {title} - {status} [/bold cyan]")
    
        elif user_inp == 3:
            console.print("[bold green] Provide the task id of the task you want to mark as completed: [/bold green]")
            try: 
                task_id = int(input())
            except ValueError as e:
                console.print("[bold red] Invalid task id [/bold red]")
                continue 
            complete_taskId = task_service.complete_task(task_id)
            if complete_taskId:
                console.print("[bold cyan] Task Completed [/bold cyan]")
            else: 
                console.print("[bold red] Invalid task id [/bold red]")
    
        elif user_inp == 4:
            console.print("[bold green] Provide the task id of the task you want to delete: [/bold green]")
            try: 
                task_id = int(input())
            except ValueError as e:
                console.print("[bold red] Invalid task id [/bold red]")
                continue 
            delete_taskId = task_service.delete_task(task_id)
            if delete_taskId:
                console.print("[bold cyan] Task Deleted [/bold cyan]")
            else: 
                console.print("[bold red] Invalid task id [/bold red]")

        elif user_inp == 5:
            console.print("[bold green] Goodbye [/bold green]")
            break

        else:
            console.print("[bold red] Enter a valid digit between 1 to 5 [/bold red]")


if __name__ == "__main__":
    main()