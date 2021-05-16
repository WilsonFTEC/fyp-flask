# fyp-flask

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Running the App</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project is the Web Application which includes all features described in Group L. Tester can login the admin's account by the following information: 
  ```sh
  email: admin@email.com
  password: gWWgWRbAs!BaE4E
  ```
Tester can register a new account for testing purpose or just login the demo account:
  ```sh
  email: demo@email.com
  password: demo1155108626
  ```

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

It is recommended to run the app in a vitual environment and install the packages in it:
  ```sh
  python3 -m venv venv
  ```
  ```sh
  source venv/bin/activate
  ```
  ```sh
  pip install -r requirements.txt
  ```

### Running the App
Before running the app, please make sure the directory is correct.
1. Set up the environment
   ```sh
   export FLASK_APP=fyp
   export FLASK_DEBUG=1
   ```

2. Enter the project path
   ```sh
   cd fyp-flask
   ```

3. Run the App
  ```sh
  flask run
  ```
