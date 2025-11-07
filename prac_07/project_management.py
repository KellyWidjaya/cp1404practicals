"""
CP1404/CP5632 Practical - Client code to use the Project class.
Estimate: 50 minutes
Actual:   40 minutes
"""

from prac_07.project import Project
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
            print("save projects")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            print("filter projects by date")
        elif choice == "a":
            print("add new project")
        elif choice == "u":
            update_project(projects)
        else:
            print("invalid choice")

        print(MENU)
        choice = input(">>> ").lower()
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

main()