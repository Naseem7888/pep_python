def create_employee(employees):
    try:
        name = input("Enter the name: ")
        if not name.strip():
            print("Error: Name cannot be empty.")
            return
        age = int(input("Enter the age: "))
        salary = float(input("Enter the salary: "))
        if age <= 0 or salary < 0:
            print("Error: Age must be positive, and salary cannot be negative.")
            return
        employee = {"name": name, "age": age, "salary": salary}
        employees.append(employee)
        print(f"\nSuccess: Employee '{name}' created.")
    except ValueError:
        print("\nError: Invalid input. Age and salary must be numbers.")
def display_employees(employees):
    if not employees:
        print("\nNo employees to display.")
        return
    print("\n--- Employee List ---")
    for i, emp in enumerate(employees, 1):
        print(f"{i}. Name: {emp['name']}, Age: {emp['age']}, Salary: ${emp['salary']:.2f}")
    print("---------------------\n")
def raise_salary(employees):
    if not employees:
        print("\nNo employees found.")
        return
    name_to_find = input("Enter the name of the employee to raise salary for: ")
    employee_found = None
    for emp in employees:
        if emp['name'].lower() == name_to_find.lower():
            employee_found = emp
            break
    if employee_found:
        try:
            raise_amount = float(input(f"Enter the amount to raise salary for {employee_found['name']}: "))
            if raise_amount < 0:
                print("Error: Raise amount cannot be negative.")
                return
            employee_found['salary'] += raise_amount
            print(f"\nSuccess: Salary for {employee_found['name']} was raised.")
            print(f"New Salary: ${employee_found['salary']:.2f}")
        except ValueError:
            print("\nError: Invalid input. Raise amount must be a number.")
    else:
        print(f"\nError: Employee with name '{name_to_find}' not found.")
def main():
    employees = []
    while True:
        print("\n--- Employee Management System ---")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            create_employee(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            raise_salary(employees)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
