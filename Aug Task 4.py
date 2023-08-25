import random

class Employee:
    def __init__(self):
        self.emp_id = random.randint(1, 9999)
        self.emp_location = random.choice(["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"])
        self.emp_salary = random.randint(20000, 150000)

    def __str__(self):
        return f"Emp Id: {self.emp_id}\nEmp Location: {self.emp_location}\nEmp Salary: {self.emp_salary}\n"

def generate_employee_details(num_employees):
    for i in range(num_employees):
        yield Employee()

def main():
    try:
        num_employees = int(input("Enter the number of employee details to generate: "))
        employee_generator = generate_employee_details(num_employees)
        employee_list = list(employee_generator)

        print("\nEmployee Details:")
        print("=================")

        for employee in employee_list:
            print(employee)

    except ValueError as e:
        print(f"{e}")

if __name__ == "__main__":
    main()
