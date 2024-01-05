<h1>FastAPI Project: Authentication and User CRUD</h1>

<h3>Project Overview:</h3>

<ul>
    <li><b>Description:</b> FastAPI project with JWT token-based authentication and User CRUD operations.</li>
    <li><b>Run Command:</b> <code>uvicorn main:app --reload</code></li>
</ul>

<h3>Key Features:</h3>

<p><b>Authentication:</b></p>
<ul>
    <li>Implements JWT token-based authentication.</li>
    <li>Securely handles user authentication with token generation.</li>
</ul>

<p><b>User CRUD Operations:</b></p>
<ul>
    <li>Connects to a SQL database using SQLAlchemy.</li>
    <li>Defines models for user data.</li>
    <li>Implements schemas for input and output validation.</li>
    <li>Supports SignUp with hashed password storage.</li>
</ul>

<h3>Folder Structure:</h3>

<pre>
  <code>app/
  ├── backend/
  │ ├── database.py
  │ ├── settings.py 
  ├── models/
  │ ├── user_model.py
  ├── routers/
  │ ├── auth_router.py
  ├── schemas/
  │ ├── user_schemas.py
  ├── services/
  │ ├── auth_service.py
  └── main.py</code>
</pre>


<h3>How to Run:</h3>

<p>Execute the command <code>uvicorn main:app --reload</code> to run the FastAPI application.</p>

<h3>Note:</h3>

<ul>
    <li>Ensure to install required dependencies before running (<code>pip install -r requirements.txt</code>).</li>
    <li>The project focuses on secure user authentication and provides CRUD functionalities for user management.</li>
    <li>Utilizes SQL Alchemy for database interactions.</li>
    <li>Incorporates password hashing for enhanced security.</li>
</ul>

<h3>Contributing:</h3>

<ul>
    <li>Fork the repository, make your changes, and submit a pull request.</li>
    <li>Contributions and improvements are welcome!</li>
</ul>

<h3>Disclaimer:</h3>

<p>This project is for educational purposes and to demonstrate best practices in FastAPI development.</p>

<hr>
