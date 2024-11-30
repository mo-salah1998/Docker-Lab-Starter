from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
 
app = Flask(__name__)
 

db_config = {
    'user': 'root',
        'password': 'root',
        'host': 'docker-lab-starter-db-1',
        'port': '3306',
        'database': 'taskdb'
}
print(db_config)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**db_config)


tasks = [
    "Finish the Flask tutorial",
    "Review Docker basics",
    "Create a task management app"
]


@app.route('/')
def index():
    """Display all tasks."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()  # Fetch all rows from the query
        
        print(tasks)
    except Exception as e:
        print(f"Database error: {e}")
        tasks = []  # Fallback to an empty list if the query fails
    finally:
        cursor.close()
        connection.close()  # Close the database connection
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task."""
    task = request.form.get('task')  # Retrieve the task from the form
    print(task)

    connection = get_db_connection()  # Get a database connection
    cursor = connection.cursor()
    try:
        # Use a parameterized query to prevent SQL injection
        cursor.execute("INSERT INTO tasks (name) VALUES (%s)", (task,))
        connection.commit()  # Commit the transaction
    except Exception as e:
        print(f"Error while adding task: {e}")
        connection.rollback()  # Rollback if an error occurs
    finally:
        cursor.close()
        connection.close()  # Always close the connection

    return redirect(url_for('index'))  # Redirect to the index route


if __name__ == "__main__":
    app.run(host='0.0.0.0')