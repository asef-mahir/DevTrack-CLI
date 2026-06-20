from app.database import init_db
from app.ui import task_menu
from app.ui.common import console, wait_for_menu


def main():
    init_db.initialize_database()

    while True:
        console.clear()
        console.print("[bold green]Welcome to your personal Task Manager [/bold green]")
        console.print("[bold green]-------------- DevTack -------------- [/bold green]")
        print("\n")

        console.print("[bold yellow]1. Add a Task [/bold yellow]")
        console.print("[bold yellow]2. Show List of All Tasks [/bold yellow]")
        console.print("[bold yellow]3. Complete a Task [/bold yellow]")
        console.print("[bold yellow]4. Delete a Task [/bold yellow]")
        console.print("[bold yellow]5. Exit [/bold yellow]")

        try: 
            user_inp = int(console.input("[bold yellow]Choose an option: [/bold yellow]"))
        except ValueError:
            console.print("[bold red]Try again with a valid digit between 1 to 5 [/bold red]")
            continue 

        if user_inp == 1:
            task_menu.add_task_flow()
    
        elif user_inp == 2:
            task_menu.list_tasks_flow()
    
        elif user_inp == 3:
            task_menu.complete_task_flow()
    
        elif user_inp == 4:
            task_menu.delete_task_flow()

        elif user_inp == 5:
            console.print("[bold green]Goodbye [/bold green]")
            break

        else:
            console.print("[bold red]Enter a valid digit between 1 to 5 [/bold red]")
            wait_for_menu()


if __name__ == "__main__":
    main()
