from app.database.connection import get_connection

def add_task(title_tsk):
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title)
        VALUES (%s)                         
        """ ,
        (title_tsk,)  
    )
    # The %s is a placeholder for the value of title_tsk, which is passed as a single element tuple (title_tsk,). This helps prevent SQL injection attacks by ensuring that the value is properly escaped.

    new_task_id = cursor.lastrowid

    connection.commit()
    cursor.close()
    connection.close()
    
    return new_task_id


def list_tasks(): 
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        #here, returning an empty list instaed of None so that even if i loop over the returned result, it won't crash
        return []
    
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id, title, status, created_at, completed_at
        FROM tasks 
        """
    )
    tasks = cursor.fetchall()

    # here, connection.commit() is not needed cz we're not modifying anything. it's just select statement. 
    cursor.close()
    connection.close()

    return tasks


def complete_task(task_id):
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return False
    
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET status = 'completed', completed_at = NOW()
        WHERE id = %s
        """
        , (task_id,)
    ) 

    total_row_affected = cursor.rowcount
    
    connection.commit()
    cursor.close()
    connection.close()

    return total_row_affected > 0


def delete_task(task_id):
    connection = get_connection()
    if not connection:
        print("Failed to connect to Database")
        return False
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM tasks 
        WHERE id = %s 
        """
        , (task_id,) 
    )

    total_row_affected = cursor.rowcount

    connection.commit()
    cursor.close()
    connection.close()

    return total_row_affected > 0