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
This project is the Web Application which includes all features described in Group L. All features have been demostrated during the presentation.

* Since the chatbot has been expired, it is not able to test the function now.

* Since google drive can only accessed by the account owner, tester is not able to login the account and see the change. However, the function for prediction can still work locally.

* Pictures for testing are placed in ```group-l-webapp-code-submission/fyp-flask/fyp/data```

Tester can login the admin's account by the following information: 
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

It is recommended to run the app in ubuntu with a python vitual environment and install the packages in it:
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
Before running the app, please make sure the current directory is ```group-l-webapp-code-submission```.
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

4. Click on http://127.0.0.1:5000

5. Press F12 enter developer mode of the browser and set the resolution as iphone X

4. Terminate the server by CTRL + C
