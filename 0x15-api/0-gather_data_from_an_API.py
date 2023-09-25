import requests
import sys

# Function to fetch employee TODO list progress
def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        if employee_response.status_code != 200:
            print(f"Error: Employee with ID {employee_id} not found.")
            return

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Display progress information
        print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
        print(f"{employee_data['name']}:", end=' ')

        for task in todo_data:
            if task['completed']:
                print("\n\t", task['title'])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
