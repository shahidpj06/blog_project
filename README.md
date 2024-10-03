<h1>Blog Project</h1>

  <h2>Project Overview</h2>
  <p>
    The Blog Project is a web application built using Python Django for managing user-generated content such as blog posts. It includes a fully responsive front-end built with Tailwind CSS and a PostgreSQL database for managing user data and blog posts. The application supports user authentication, CRUD operations on blog posts, and Docker for containerization and easy deployment.
  </p>

  <h2>Features</h2>
  <ul>
    <li>User authentication (login, signup, profile management)</li>
    <li>CRUD operations for blog posts (Create, Read, Update, Delete)</li>
    <li>Responsive front-end using Tailwind CSS</li>
    <li>Dockerized setup for easy deployment</li>
  </ul>

  <h2>Technologies Used</h2>
  <ul>
    <li><strong>Backend:</strong> Python, Django</li>
    <li><strong>Frontend:</strong> Tailwind CSS, Vanilla JavaScript</li>
    <li><strong>Database:</strong> PostgreSQL</li>
    <li><strong>Containerization:</strong> Docker</li>
  </ul>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/shahidpj06/blog_project</code></pre>

  <h3>2. Navigate to the Project Directory</h3>
  <pre><code>cd blog_project</code></pre>

  <h3>3. Create and Activate a Virtual Environment (For Local Setup)</h3>
  <p>For a local development environment (without Docker), you'll need to set up a Python virtual environment:</p>
  <pre><code>
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (on macOS/Linux)
source venv/bin/activate

# Activate the virtual environment (on Windows)
venv\Scripts\activate
  </code></pre>

  <h3>4. Install Dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>5. Set Up the Database</h3>
  <pre><code>
# Migrate database
python manage.py migrate
  </code></pre>

  <h3>6. Create a Superuser</h3>
  <p>Create an admin user to access the Django admin interface:</p>
  <pre><code>python manage.py createsuperuser</code></pre>

  <h3>7. Run the Application Locally</h3>
  <pre><code>python manage.py runserver</code></pre>
  <p>Visit <code>http://127.0.0.1:8000/</code> in your browser.</p>

  <h3>6. Front End Setup</h3>
  <p>open a new terminal</p>
  <pre><code>python manage.py tailwind start</code></pre>

  <h2>Running the Application with Docker</h2>

  <h3>1. Install Docker</h3>
  <p>Ensure Docker is installed on your machine. You can download it from <a href="https://www.docker.com/products/docker-desktop">here</a>.</p>

  <h3>2. Build and Run the Docker Containers</h3>
  <pre><code>docker-compose up --build</code></pre>
  <p>This will build the Docker image and run the containers for the database and the web application.</p>

  <h3>3. Access the Application</h3>
  <p>Once the Docker containers are running, you can access the application at <code>http://localhost:8000/</code>.</p>

  <h3>4. Stopping the Containers</h3>
  <pre><code>docker-compose down</code></pre>
  <p>This will stop and remove the containers when you're finished.</p>


  <h2>File Structure</h2>
  <p>The following is the file structure of the project:</p>
  <pre><code>
blog_project/
├── blog_project/           # Django project configuration
├── blog/                   # Main blog application
├── theme/                  # Frontend theme files (Tailwind CSS, JS)
├── Dockerfile              # Docker setup for the web app
├── docker-compose.yml      # Docker Compose for multi-container setup
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
  </code></pre>
