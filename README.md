To run this project (instructions for windows, linux/Mac may slightly vary):

    Note: Make sure you have the ability to run python files theough your command line.

    Step 1: Clone the repository to a local directory.
        Steb 1a. Run command: Git clone https://gitlab.com/Lexrocker/project-alpha-apr.git
    
    Step 2: Run a virtual enviorment so that requirements downloads do not effect your system
        Step 2a. Run command to create virtual enviorment: python -m venv .venv
        Step 2b: Run command to start virtual enviorment: .\.venv\scripts\activate.ps1
    
    Step 3: Start the Django Server
        Step 3a: Run command: python manage.py runserver

What it does:
    This project is a simple Django exploration and the first website I created from scratch. 
    The website allows you to create a project and assign tasks to yourself or other users. 
    The person who is assigned the task can mark it as complete and the project creator and 
    all users who have been assigned tasks on the project can view all tasks for that project, 
    who they are assigned to, and if they have been completed.

Technologies Utilized:
    Python, Django Framework, Monolithic Application.
