#assignment1.py
# This program manages employee records with options to add, view, and search employees.

#This function adds an employee to the dictionary.
def add_employee(d):
    while(True):
        emp_id=int(input('Enter employee ID:'))
        v={}
        v["name"]=input("Enter employee name:")
        v["age"]=int(input("Enter age of employee:"))
        v["department"]=input("Enter employee department:")
        v["salary"]=int(input("Enter Employee Salary:"))
        if(emp_id not in d):
            d[emp_id]=v
            print("employee was successfully added")
            break
        else:
            print("Emp ID already exists enter a new emp id")

# This function displays all employees in the dictionary.
def view_employee(d):
    if(len(d)==0):
        print("No employees to display")
        return
    print("ID\tname\tage\tdepartment\tsalary")
    for i in d:
        print(i, end="\t")
        v=d[i]
        for j in v:
            print(v[j],end='\t')
        print("\n")

#This function searches for an employee by ID in the dictionary.
def search_employee(d):
    emp=int(input("Enter the employee id you need to search: "))
    try:
        print(d[emp])
    except:
        print("Employee not found")

#This function displays the main menu and handles user choices.
def main_menu():
    d={}
    print("select a no. between 1 to 4\n1. Add Employee\n2.View All Employees\n3.Search for Employee\n4.exit")
    while(True):
        choice=int(input('Enter your choice:'))
        if(choice==1):
            add_employee(d)
        if(choice==2):
            view_employee(d)
        if(choice==3):
            search_employee(d)
        if(choice==4):
            print("Thank You")
            break

main_menu()