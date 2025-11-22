"""
CP1404/CP5632 Practical - Client code to use the Project class.
Estimate: 50 minutes
Actual:   1 hour 50 minutes
"""

from prac_07.project import Project
from operator import attrgetter
import datetime

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    """Project management menu program."""
    print("Welcome to Pythonic Project Management")
    filename = DEFAULT_FILENAME
    projects = load_projects(filename)
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("invalid choice")

        print(MENU)
        choice = input(">>> ").lower()
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ")
    if save_choice == "y":
        save_projects(DEFAULT_FILENAME, projects)

    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            name, date_string, priority, cost, completion = line.split("\t")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(name, date, int(priority), float(cost), int(completion))
            projects.append(project)

    print(f"Loaded {len(projects)} projects from {filename}")

    return projects

def display_projects(projects):
    """Print project details."""
    print("Incomplete projects:")
    for project in sorted(projects):
        if not project.is_complete():
            print(f"  {project}")

    print("Completed projects:")
    for project in sorted(projects):
        if project.is_complete():
            print(f"  {project}")


def update_project(projects):
    """Change the priority and/or completion percentage of project."""
    for i, project in enumerate(projects):
        print(i, project)

    index = int(input("Project choice: "))
    project = projects[index]
    print(project)

    new_completion = input("New Percentage: ")
    if new_completion != "":
        project.completion = int(new_completion)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)

def add_project(projects):
    """Get details for a new project and add it to the list."""
    print("Let's add a new project")

    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    new_project = Project(name, date, priority, cost, completion)
    projects.append(new_project)

def filter_projects(projects):
    """Get date and display projects starting after that date."""
    date_threshold_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date_threshold = datetime.datetime.strptime(date_threshold_string, "%d/%m/%Y").date()

    filtered_project = [project for project in projects if project.date >= date_threshold]
    filtered_project.sort(key=attrgetter("date"))
    for project in filtered_project:
        print(project)

def save_projects(filename, projects):
    """Write the list of Project objects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost}\t{project.completion}", file=out_file)
    print(f"Projects saved to {filename}")

main()