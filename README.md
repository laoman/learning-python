# Python 101 - Flask, Docker, and MySQL Integration Project

This project serves as a hands-on introduction to building and containerizing a full-stack web application. It covers the fundamentals of creating a Python Flask backend, connecting it to a MySQL database, and managing the entire stack with Docker Compose.

## Key Concepts Covered

### 1. Python Flask Web Application
- **Basic Application Structure**: Setting up a simple Flask app with routes.
- **Routing**: Defining URL endpoints (`@app.route`) for different functionalities, including handling `GET` and `POST` requests.
- **Templating with Jinja2**: Creating dynamic HTML pages (`render_template`) by passing data from the backend to the frontend.
- **Handling Form Data**: Processing user input submitted through web forms (`request.form`).

### 2. Database Integration with MySQL
- **Connecting to a Database**: Using the `mysql-connector-python` library to establish a connection between the Flask app and a MySQL server.
- **CRUD Operations**:
    - **Create**: Executing `CREATE TABLE IF NOT EXISTS` to define the database schema programmatically.
    - **Update/Insert**: Inserting new records into the database based on form submissions.
    - **Read**: Querying the database to fetch and display records on the web page.
- **Secure Credentials**: Reading database credentials (host, user, password) from environment variables rather than hardcoding them in the source code.

### 3. Containerization with Docker & Docker Compose
- **Multi-Service Orchestration**: Using a `docker-compose.yml` file to define, configure, and run a multi-container application (Flask app, MySQL, Jenkins).
- **Service Dependencies**: Managing the startup order of services using `depends_on` and `healthcheck` to ensure the database is fully ready before the application tries to connect to it.
- **Persistent Data**: Using Docker volumes (`volumes:`) to persist MySQL database data even when containers are removed or restarted.
- **Networking**: Understanding how services within the same Docker Compose network can communicate with each other using their service names as hostnames.
- **Port Mapping**: Exposing container ports to the host machine to make the web application and Jenkins accessible from a browser.

### 4. Version Control (Git)
- **Ignoring Files**: Using a `.gitignore` file to prevent unnecessary or sensitive files from being committed to the repository. This includes Python cache (`__pycache__`), virtual environments, IDE configuration files, and OS-specific files like `.DS_Store`.

### 5. Continuous Integration (CI/CD) with Jenkins
- **Automated Builds**: Setting up a Jenkins container using a separate `docker-compose-jenkins.yml` file to create an environment for automating the building, testing, and deployment of the application.

## How to Run This Project

1.  **Prerequisites**: Ensure you have Docker and Docker Compose installed on your machine.
2.  **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd learning-python
    ```
3.  **Run the Application**:
    ```bash
    docker-compose up --build -d
    ```
4.  **Access the Services**:
    -   **Web Application**: Open your browser and navigate to [http://localhost:80](http://localhost:80).
    -   **Jenkins**: Open your browser and navigate to [http://localhost:8081](http://localhost:8081).