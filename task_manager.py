# Imported the datetime module to use the current date
from datetime import date


# Login function used for the user to be able to login
# Opens the user.txt file and separates each line into individual list item
def login(login_user):
    with open("user.txt", "r") as user_file:
        user_content = user_file.read()
        user_content = user_content.splitlines()

    user_info = []
    login_loop = True

    # Loops through each item in the file and splits it further
    # and then adds each individual item to a new list
    for all_details in user_content:
        user_details = all_details.split(", ")

        for individual_details in user_details:
            user_info.append(individual_details)

    # Loops through this section of code continuously until the user has logged in successfully
    # Checks if the entered username is in the user.txt file and asks the user to enter the password
    # If the username is not found an error is displayed and the code is looped through again
    while login_loop:
        if login_user in user_info[::2]:
            login_password = input("Please enter your password: ")

            # Checks if the password the user entered is in the user.txt file
            # and the says the login was successful and cancels the while loop
            # If the password is not found an error is displayed and the user is asked to enter a password again
            if login_password in user_info[1::2]:
                print("Login successful.")
                login_loop = False
                return user_info

            else:
                print("\t\tIncorrect password.")

        else:
            print("\t\tUsername not found.")
            login_user = input("Please enter your username: ")


# reg_user function used to register new users
# Asks the user to enter the username to be registered
def reg_user(user_list):
    new_username = input("Please enter the username to be registered: ")

    # Checks to make sure the user has not been registered already
    # If the user has been registered an error is displayed
    # Asks the user to enter a password for the new username and to confirm it
    if new_username not in user_list[::2]:
        new_password = input("Please enter a password for that username: ")
        confirm_password = input("Please enter the password again to confirm it: ")

        # If the password match the user is added to the user.txt file and a confirmation statement is printed out
        # If the passwords do not match an error message is displayed
        if new_password == confirm_password:
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username}, {confirm_password}")
            print("\tUser has been registered.")
        else:
            print("The passwords do not match.")
    else:
        print("That user has already been registered.")


# add_task function is used to add tasks for the users
# Asks the user to input all the info concerning the new task to be added
# Opens the tasks.txt file and adds all the info the user had entered to it
# Prints a confirmation statement to tell the user that adding the task was successful
def add_task():
    task_assigned = input("\nPlease enter who the task will be assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please enter a short description of the task: ")
    task_due = input("Please enter when the task is due: ")
    assigned_date = date.today().strftime("%d-%m-%Y")
    task_completed = "No"

    with open("tasks.txt", "a") as task_file:
        task_file.write(
            f"\n{task_assigned}, {task_title}, {task_description}, {assigned_date}, {task_due}, {task_completed}")
    print("\tTask added successfully.")


# view_all function is used to display all the current tasks to the user
# opens the tasks.txt file and then splits all the information in it,
# It then prints out the info into a readable manner for each task
def view_all():
    with open("tasks.txt", "r") as tasks:
        task_contents = tasks.read()
        task_contents = task_contents.splitlines()

    for task in task_contents:
        task_list = task.split(", ")

        print(f"-------------------------------------------------------------------------------------\n"
              f"Task:\t\t\t\t{task_list[1]}\n"
              f"Assigned to:\t\t{task_list[0]}\n"
              f"Date assigned:\t\t{task_list[3]}\n"
              f"Due date:\t\t\t{task_list[4]}\n"
              f"Task complete?\t\t{task_list[5]}\n"
              f"Task description:\n"
              f"\t{task_list[2]}")
    print("-------------------------------------------------------------------------------------")


# view_mine function is used to view all the tasks assigned to the current user
# looks in the tasks.txt file for any tasks assigned to the current user and displays them all in a readable manner
def view_mine(login_user):
    with open("tasks.txt", "r") as tasks:
        task_contents = tasks.read()
        task_contents = task_contents.splitlines()

    found_task = False
    viewing_tasks = False

    for task in task_contents:
        task_number = task_contents.index(task)
        task_list = task.split(", ")

        if task_list[0] == login_user:
            print(f"-------------------------------------------------------------------------------------\n"
                  f"Task number:\t\t{task_number + 1}\n"
                  f"Task:\t\t\t\t{task_list[1]}\n"
                  f"Assigned to:\t\t{task_list[0]}\n"
                  f"Date assigned:\t\t{task_list[3]}\n"
                  f"Due date:\t\t\t{task_list[4]}\n"
                  f"Task complete?\t\t{task_list[5]}\n"
                  f"Task description:\n"
                  f"\t{task_list[2]}")

            found_task = True
            viewing_tasks = True

    # Loops through this section of code till the user exits it
    # If a task is found for the user it prints out the information for it
    # If no tasks are found an error is displayed
    # The user is asked if the want to look at a specific task or if they want to return to the main menu
    # An error is displayed if the task number they entered doesn't exist
    while viewing_tasks:
        if found_task:
            print("-------------------------------------------------------------------------------------")
            specific_task = int(
                input("\nTo look at a specific task enter its task number or -1 to return to the main menu: "))

            for task in task_contents:
                task_number = task_contents.index(task)
                task_list = task.split(", ")

                if specific_task - 1 == task_number:
                    print(f"-------------------------------------------------------------------------------------\n"
                          f"Task number:\t\t{task_number + 1}\n"
                          f"Task:\t\t\t\t{task_list[1]}\n"
                          f"Assigned to:\t\t{task_list[0]}\n"
                          f"Date assigned:\t\t{task_list[3]}\n"
                          f"Due date:\t\t\t{task_list[4]}\n"
                          f"Task complete?\t\t{task_list[5]}\n"
                          f"Task description:\n"
                          f"\t{task_list[2]}\n"
                          f"-------------------------------------------------------------------------------------")

                elif specific_task == -1:
                    viewing_tasks = False
                    print("\tReturning to main menu.")

                else:
                    print("\tError. Task number not found.")

    if not found_task:
        print("\nNo tasks were found for the current user")


# generate_reports function is used to create files that holds information on all the tasks and users
def generate_reports(task, user):
    num_tasks = len(task)
    num_incomplete = 0
    num_complete = 0
    num_overdue = 0

    # Loops through each item in the tasks.txt file and counts how many completed and incompleted tasks there are
    # Searches for any tasks that are overdue adn still incomplete
    for value in task:
        task_list = value.split(", ")

        num_incomplete += task_list.count("No")
        num_complete += task_list.count("Yes")

        if task_list[5] == "No" and task_list[3] > task_list[4]:
            num_overdue += 1

    # Calculates the percentages of complete, incomplete and overdue tasks
    percent_complete = (num_complete / num_tasks) * 100
    percent_incomplete = (num_incomplete / num_tasks) * 100
    percent_overdue = (num_overdue / num_tasks) * 100

    # Saves all of the info calculated into the task_overview.txt file
    with open("task_overview.txt", "w") as overview:
        overview.write(f"Overview of tasks:\n"
                       f"\tTotal number tasks:\t\t\t\t\t\t\t\t{num_tasks}\n"
                       f"\tTotal completed tasks:\t\t\t\t\t\t\t{num_complete}\n"
                       f"\tTotal number incomplete tasks:\t\t\t\t\t{num_incomplete}\n"
                       f"\tTotal number tasks incomplete and overdue:\t\t{num_overdue}\n"
                       f"\tPercent of complete tasks:\t\t\t\t\t\t{int(round(percent_complete, 0))}%\n"
                       f"\tPercent of incomplete tasks:\t\t\t\t\t{int(round(percent_incomplete, 0))}%\n"
                       f"\tPercent of incomplete and overdue tasks:\t\t{int(round(percent_overdue, 0))}%\n")

    with open("user_overview.txt", "w") as overview:
        overview.write("Overview of users:\n")

        # Loops through each item in the user.txt file
        for details in user:
            user_list = details.split(", ")

            user_tasks = 0
            percent_tasks = 0
            user_complete = 0
            user_incomplete = 0
            user_overdue = 0

            # Counts all the counts that are complete, incomplete or overdue for the specific users
            for value in task:
                task_list = value.split(", ")
                user_tasks += task_list.count(user_list[0])

                if task_list[0] == user_list[0]:
                    user_complete += task_list.count("Yes")
                    user_incomplete += task_list.count("No")

                if task_list[5] == "No" and task_list[3] > task_list[4]:
                    num_overdue += 1

            # Calculates the percentages for the number of tasks that are complete, incompleted and overdue
            percent_tasks = (user_tasks / num_tasks) * 100
            if user_tasks > 0:
                user_percent_overdue = (user_overdue / user_tasks) * 100
            else:
                user_percent_overdue = 0

            if user_complete > 0:
                user_complete_percent = (user_complete / user_tasks) * 100
            else:
                user_complete_percent = 0

            if user_incomplete > 0:
                user_incomplete_percent = (user_incomplete / user_tasks) * 100
            else:
                user_incomplete_percent = 0

            # Adds all this info to the user_overview.txt file
            overview.write(f"\tOverview for {user_list[0]}:\n"
                           f"\t\tTotal number tasks assigned:\t\t\t\t\t\t\t{int(round(user_tasks, 0))}"
                           f"\n\t\tPercentage of tasks assigned:\t\t\t\t\t\t\t{int(round(percent_tasks, 0))}%"
                           f"\n\t\tTotal completed tasks for:\t\t\t\t\t\t\t\t{int(round(user_complete_percent, 0))}%"
                           f"\n\t\tPercentage of tasks incomplete:\t\t\t\t\t\t\t{int(round(user_incomplete_percent, 0))}%"
                           f"\n\t\tPercentage of incomplete and overdue tasks:\t\t\t\t{int(round(user_percent_overdue, 0))}\n")


# display_statistics function is used to display all the info in the user_overview.txt and task_overview.txt files
# If these files don't exist the generate_reports function is called to create these files
# and them display the info in them
def display_statistics(task_contents, user_contents):
    try:
        with open("task_overview.txt", "r") as task_overview:
            content_task = task_overview.read()
            print(content_task)
        with open("user_overview.txt", "r") as user_overview:
            content_user = user_overview.read()
            print(content_user)

    except FileNotFoundError:
        generate_reports(task_contents, user_contents)
        with open("task_overview.txt", "r") as task_overview:
            content_task = task_overview.read()
            print(content_task)
        with open("user_overview.txt", "r") as user_overview:
            content_user = user_overview.read()
            print(content_user)


running_program = True

login_username = input("Please enter your username: ")
users = login(login_username)

while running_program:
    if login_username == "admin":
        with open("tasks.txt", "r") as tasks_file:
            task_content = tasks_file.read()
            task_content = task_content.splitlines()

        with open("user.txt", "r") as users_file:
            user_content = users_file.read()
            user_content = user_content.splitlines()

        print(f"\nThere are {len(user_content)} users.")
        print(f"There are {len(task_content)} tasks.")

    print("\nPlease select one of the following options:\n"
          "r - register a user\n"
          "a - add task\n"
          "va - view all tasks\n"
          "vm - view my tasks")
    if login_username == "admin":
        print("gr - generate reports\n"
              "ds - display statistics")
    print("e - exit")
    options = input("")

    if options == "r":
        if login_username == "admin":
            reg_user(users)

        else:
            print("Only the admin can register a user.")

    elif options == "a":
        add_task()

    elif options == "va":
        view_all()

    elif options == "vm":
        view_mine(login_username)

    elif options == "gr":
        generate_reports(task_content, user_content)

    elif options == "ds":
        display_statistics(task_content, user_content)

    elif options == "e":
        running_program = False
