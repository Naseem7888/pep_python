employees = []
while True:
    print("1. CREATE\n2. DISPLAY\n3. RAISE SAL\n4. EXIT")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("ENTER THE NAME: ")
        age = input("ENTER THE AGE: ")
        designation = input("ENTER THE DESIGNATION (PROGRAMMER 25K / MANAGER 30K / TESTER 20K): ").upper()
        salary = 0
        if designation == "PROGRAMMER":
            salary = 25000
        elif designation == "MANAGER":
            salary = 30000
        elif designation == "TESTER":
            salary = 20000
        else:
            print("Invalid designation. Salary set to 0.")
        employees.append({"name": name, "age": age, "designation": designation, "salary": salary})
    elif choice == '2':
        if not employees:
            print("No employees to display.")
            continue
        for emp in employees:
            print(f"Name: {emp['name']}, Age: {emp['age']}, Designation: {emp['designation']}, Salary: {emp['salary']}")
    elif choice == '3':
        if not employees:
            print("No employees to raise salary for.")
            continue
        name_to_raise = input("Enter employee name to raise salary: ")
        found = False
        for emp in employees:
            if emp['name'].lower() == name_to_raise.lower():
                try:
                    raise_amount = float(input(f"Enter amount to raise salary for {emp['name']}: "))
                    emp['salary'] += raise_amount
                    print(f"New salary for {emp['name']}: {emp['salary']}")
                    found = True
                    break
                except ValueError:
                    print("Invalid amount entered.")
        if not found:
            print(f"Employee '{name_to_raise}' not found.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
