from rich.console import Console

console = Console()


def wait_for_menu():
    console.input("[bold yellow]Press Enter to return to the menu...[/bold yellow]")


def should_repeat_action(action_name):
    user_choice = console.input(f"[bold yellow]Press r to {action_name} again, or Enter to return to the menu: [/bold yellow]").strip().lower()
    return user_choice == "r"


def show_tasks_page(task_list, current_page, page_size):
    total_tasks = len(task_list)
    total_pages = (total_tasks + page_size - 1) // page_size
    start = current_page * page_size
    end = start + page_size

    console.print(f"[bold green]Tasks page {current_page + 1} of {total_pages}[/bold green]")
    for task in task_list[start:end]:
        task_id, title, status, created_at, completed_at = task
        console.print(f"[bold cyan]{task_id}. {title} - {status}[/bold cyan]")


def browse_tasks(task_list):
    page_size = 10
    current_page = 0
    should_show_page = True
    total_pages = (len(task_list) + page_size - 1) // page_size

    while True:
        if should_show_page:
            show_tasks_page(task_list, current_page, page_size)
            should_show_page = False

        if total_pages == 1:
            wait_for_menu()
            return

        user_choice = console.input("[bold yellow]n for next, p for previous, or q to return to the menu: [/bold yellow]").strip().lower()
        if user_choice == "q":
            return
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

        console.print("[bold red]Invalid option[/bold red]")
