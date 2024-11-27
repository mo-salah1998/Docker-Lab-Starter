from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
 
app = Flask(__name__)
 

# Initialize the task list with default items
tasks = [
    "Finish the Flask tutorial",
    "Review Docker basics",
    "Create a task management app"
]

@app.route('/')
def index():
    """Display all tasks."""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task."""
    task = request.form.get('task')
    if task:
        tasks.append(task)  # Add the task to the list
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')