from app.models import task_model 

def add_task(title):
    clean_title = title.strip() 
    if clean_title == "" or len(clean_title) > 255:
        return False          
    new_task_id = task_model.add_task(clean_title)
    return new_task_id

def list_tasks(): 
    tk_list = task_model.list_tasks()
    return tk_list

def complete_task(task_id):
    if not isinstance(task_id, int) or task_id <= 0:
        return False 
    return task_model.complete_task(task_id)

def delete_task(task_id):
    if not isinstance(task_id, int) or task_id <= 0:
        return False
    return task_model.delete_task(task_id)
