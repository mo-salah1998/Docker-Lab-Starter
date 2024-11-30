# Docker Lab Starter

Welcome to the Docker Lab Starter project! This repository is designed to help you get hands-on experience with containerizing an application using Docker. The goal is to take an existing application, test it locally, and then create a `Dockerfile` to containerize the application.

---

## Objectives

By completing this assessment, you will:
1. Understand the application's functionality by testing it locally.
2. Learn to create a `Dockerfile` to containerize the application.
3. Run the application inside a Docker container.
4. Use Docker Compose to manage a multi-container setup.

---

## Getting Started

### Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.9 or later)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### Step 1: Clone the Repository
First, clone the project to your local machine:

```bash
git clone https://github.com/mo-salah1998/Docker-Lab-Starter.git
cd Docker-Lab-Starter
```

---

### Step 2: Run the Application Locally
To understand the application's functionality:

1. Navigate to the project directory:
   ```bash
   cd Docker-Lab-Starter
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to interact with the application.

Take a moment to explore the app and understand what it does.

---

### Step 3: Containerize the Application
Your task is to create a `Dockerfile` to containerize this application. Follow these steps:

1. **Create a Dockerfile**  
   - Inside the project directory, create a file named `Dockerfile`.
   - Write a `Dockerfile` to containerize the application. Here are some tips:
     - Use a Python base image (e.g., `python:3.11-slim`).
     - Copy the application files into the container.
     - Install dependencies using `pip`.
     - Expose port `5000`.
     - Set the command to run `main.py`.

2. **Build the Docker Image**  
   Build the image using the following command:
   ```bash
   docker build -t docker-lab-starter .
   ```

3. **Run the Container**  
   Run the application in a container:
   ```bash
   docker run -d -p 5000:5000 docker-lab-starter
   ```

4. **Test the Application in a Container**  
   Open your browser and go to `http://127.0.0.1:5000` to verify that the application runs correctly in a container.

5. **Push the Image to a dockerHub new repo**  


---

### Step 4: Adapt the Application to Use MySQL
To enhance the application, you will persist tasks in a MySQL database.

1. **Modify the Flask App**  
   Update the Flask application (`main.py`) to connect to a MySQL database and store tasks. Replace the in-memory `tasks` list with database operations.

   Example changes:
   - Use `mysql.connector` to connect to the database.
   - Fetch tasks from the database for display.
   - Insert new tasks into the database.

---

### Step 5: Create a Docker Compose Setup

1. **Define `docker-compose.yml`**  
   Create a `docker-compose.yml` file to manage both the Flask app and the MySQL database.


2. **Build and Start Containers**  
   Use Docker Compose to build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. **Test the Application**  
   Open your browser and go to `http://127.0.0.1:5000`. Verify that tasks are stored in the MySQL database.

---


## Submission
Once you have successfully containerized the application:

1. Make sure your `Dockerfile` is included in the project directory.
2. Document your steps in a `README.md` file inside the project.
3. Push your changes to a GitHub repository and share the link.

---

## Hints and Tips
- Refer to the [Docker Documentation](https://docs.docker.com/) if you need help with Docker commands.
- Check for errors during the build or run process and debug accordingly.
- If you are new to Flask or Python, take some time to review the code in `main.py`.
- Test database connectivity using the `mysql` CLI or a GUI client like MySQL Workbench.
- Check for errors during container startup and debug logs with `docker-compose logs`.


---

## Learning Outcomes
By completing this assessment, you will gain hands-on experience in:
- Testing a Python web application.
- Writing and understanding `Dockerfile` syntax.
- Building and running Docker containers.
- Containerizing a real-world application.
- Using Docker Compose for multi-container setups.
- Persisting data in a relational database.
- Managing real-world application workflows with Docker.

---

🚀 Happy coding & learning ! 🚀
