
A CRUD Todo API


STEPS TO REPRODUCE THIS CODE
1. Clone this repo to your machine. Ensure you have `python` and `pipenv` installed on your machine

2. cd into the folder and run the following code block.
    
    ```
       >> pipenv shell 
       >> pipenv install
    ```
    
The first code snippet will startup a virtual environment while the second code snippet will install all the dependencies for the project

3. execute the code below to startup the server
    
    ```
    >> python manage.py runserver
    ```
    
    The code will create an instance of the server which is accessible through localhost:8000

4. To test the API, these are the various endpoints
    
    a.  `localhost:8000/todo/`    ---To POST new Tasks and GET all todo tasks. Fields to populate when making POST requests are `title`, `body`, `date_created`, `isCompleted`. Although, the fields `date_created` and `isCreated` have been set by default to the current date and `False` respectively.
    
    b.  `localhost:8000/todo/<integer>/`  ---To GET,PUT and DELETE specific tasks in details. `<integer>` there refers to whole numbers
    
    c.  `localhost:8000/todo/days/`      ---To access all tasks peculiar to that day
    
    d.   `localhost:8000/users/signup/`    ---To register a user on the API. Fields to populate are   `username`,`email` and `password`
  
    e.  `localhost:8000/users/login/`    ---To login a user and grant access to other features of the API. Fields to populate are `username` and `password`.
    
    f.  `localhost:8000/users/logout/`    ---To logout a user. Make a POST request and the following fields to the header. Key = `Authorization` Value = `Token c50c6e7dddce26ae0b593ce979e8b78be908d341ae4e66c6a64c29232645a463`
    

The API restricts vital features like creating tasks, updating tasks, and deleting tasks to authenticated users only. Non authenticated users can only view tasks.
