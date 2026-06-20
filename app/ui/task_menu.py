from app.services import task_service
from app.ui.common import browse_tasks, console, should_repeat_action, show_tasks_page, wait_for_menu


def add_task_flow():
    while True:
        task_title = console.input("[bold green]Enter Task Name: [/bold green]")
        new_task_id = task_service.add_task(task_title)
        if new_task_id:
            console.print(f"[bold cyan]New task added with task id : {new_task_id} [/bold cyan]")
        else:
            console.print("[bold red] Invalid title [/bold red]")
        if not should_repeat_action("add another task"):
            break


def list_tasks_flow():
    task_list = task_service.list_tasks()
    if not task_list:
        console.print("[bold green]No Task Available[/bold green]")
        wait_for_menu()
        return

    console.print("[bold green]Displaying the list of the tasks: \n [/bold green]")
    browse_tasks(task_list)


def choose_task_id(action_name):
    user_choice = console.input(f"[bold green]Enter task id to {action_name}, or type list: [/bold green]").strip()
    if user_choice.lower() != "list":
        try:
            return int(user_choice)
        except ValueError:
            console.print("[bold red]Invalid task id[/bold red]")
            return None

    task_list = task_service.list_tasks()
    if not task_list:
        console.print("[bold red]No tasks available[/bold red]")
        return None

    page_size = 10
    current_page = 0
    should_show_page = True
    total_pages = (len(task_list) + page_size - 1) // page_size

    while True:
        if should_show_page:
            show_tasks_page(task_list, current_page, page_size)
            should_show_page = False

        user_choice = console.input("[bold yellow]Enter task id, n for next, p for previous, or q to cancel: [/bold yellow]").strip().lower()

        if user_choice == "q":
            return None
        if user_choice == "n":
            if current_page < total_pages - 1:
                current_page += 1
                should_show_page = True
            else:
                console.print("[bold red]You are already on the last page[/bold red]")
            continue
        if user_choice == "p":
            if current_page > 0:
                current_page -= 1
                should_show_page = True
            else:
                console.print("[bold red]You are already on the first page[/bold red]")
            continue

        try:
            return int(user_choice)
        except ValueError:
            console.print("[bold red]Invalid task id[/bold red]")


def complete_task_flow():
    while True:
        task_id = choose_task_id("complete")
        if task_id is None:
            break

        complete_task_id = task_service.complete_task(task_id)
        if complete_task_id:
            console.print("[bold cyan]Task Completed [/bold cyan]")
        else:
            console.print("[bold red]Invalid task id [/bold red]")
        if not should_repeat_action("complete another task"):
            break


def delete_task_flow():
    while True:
        task_id = choose_task_id("delete")
        if task_id is None:
            break

        delete_task_id = task_service.delete_task(task_id)
        if delete_task_id:
            console.print("[bold cyan]Task Deleted [/bold cyan]")
        else:
            console.print("[bold red]Invalid task id [/bold red]")
        if not should_repeat_action("delete another task"):
            break
