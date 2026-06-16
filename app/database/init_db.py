from app.database.connection import get_connection 

def initialize_database():
    connection = get_connection()
    if connection is None:
        print("Failed to connect to the database. Initialization aborted.")
        return
    
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            status ENUM('pending', 'completed') DEFAULT 'pending',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            completed_at DATETIME NULL
            )
    """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            topic VARCHAR(255) NOT NULL,
            start_time DATETIME,
            end_time DATETIME,
            duration_minutes INT
        )
    """)

    connection.commit()

    #print("Tables created successfully.")

    cursor.close()
    connection.close()
