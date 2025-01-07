import psycopg2
connection = psycopg2.connect(
    database="crm_dev"
)

cursor = connection.cursor()
# '''
# greet the employee
# add employee
# delete employee
# update employee
# read employee


# customer id
# customer name 
# company id


# company table
# '''

running = False
welcome_message = """
Welcome to the Employee Management System.
Please choose an option:
1. Add Employee
2. Delete Employee
3. Update Employee
4. Read Employee
5. Add Company
6. Delete Company
7. Update Company
8. Read Company
9. Exit
"""


def addEmp():
    empName = input("what is the name of the employee: ")
    empEmployer = input("what is the ID of the company they work for: ")
    
    cursor.execute("INSERT INTO employees (name, company_id) VALUES (%s, %s)", [empName, empEmployer] )
    connection.commit()
    print(f"employee {empName} has been added")


def deleteEmp():
        empId = input("Enter the id of the employee you wish to delete: ")
        cursor.execute("DELETE FROM employees WHERE id = %s", [empId])
        connection.commit()


def updateEmp():
        empId = input("Enter the id of the employee you wish to update: ")
        newName = input("Enter the employees new name: ")
        newComp = input("Enter the employees new companyId: ")
        cursor.execute("UPDATE employees SET name = %s, company_id =%s WHERE id = %s", [newName, newComp, empId])
        connection.commit()
        
def readEmp():
    #formatting from the chat ghipitah 
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print(f"{'id':<5} {'| name':<10} {'| company_id|':<10}")
    print("-" * 30)  # Print a separator line
    for row in rows:
        print(f"{row[0]:<5} |{row[1]:<10}| {row[2]:<10}|")
    
    # print(cursor.fetchall())

def addCom():
    companyName = input("What is the name of the Company?")
    cursor.execute("INSERT INTO companies (name) VALUES (%s)", [companyName])
    connection.commit()
    print(f"Company {companyName} added !")

def deleteCOM():
    comId = input("Enter the id of the Company you wish to delete: ")
    cursor.execute("DELETE FROM companies WHERE id = %s", [comId])
    connection.commit()
    print(f"company deleted")

def updateCom():
    comId = input("Enter the id of the Company you wish to update: ")
    newComName = input("Enter the new name of the company: ")
    cursor.execute("UPDATE companies SET name = %s WHERE id = %s", [newComName, comId])
    connection.commit()
    
def readCom():
    cursor.execute("SELECT * FROM companies")
    rows = cursor.fetchall()
    print(f"{'id':<5} {'| name':<10}")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<10}")





    # print(cursor.fetchall())
    
    
userchoice = 999 



# connection = psycopg2.connect(
#     database="crm_dev"
# )
while int(userchoice) != 9:
    
    # """
# Welcome to the Employee Management System.
# Please choose an option:
# 1. Add Employee
# 2. Delete Employee
# 3. Update Employee
# 4. Read Employee
# 5. Add Company
# 6. Delete Company
# 7. Update Company
# 8. Read Company
# 9. Exit
# """
    userchoice = input(welcome_message)
    match int(userchoice):
        case 1:
            addEmp()
            
        case 2:
            deleteEmp()
            
        case 3:
            updateEmp()
            
        case 4:
            readEmp()   
             
        case 5:
            addCom()
            
        case 6:
            deleteCOM()
        case 7:
            updateCom()
        case 8:
            readCom()
        case 9:
            print("Exiting...") 
            connection.close()
        case _:
            print("invalid choice. do better")
            









# def quit():
#     running = False


# def start():
#     running = True
# while running :
#     userchoice = input(welcome_message)
#     # if userchoice == 1:
#         # print("woooopie")
#     match userchoice:
#         case 1:
#             print("one")
#         case 2:
#             print("two")
#         case 3:
#             print("three")
#         case 4:
#             print("four")
#         case 5:
#             print("five")
#         case 6:
#             print("six")
#         case 7:
#             print("seven")
#         case 8:
#             print("eight")
#         case 9:
#             print("Exiting...")

# start()
    # print(userchoice)
    # connection = psycopg2.connect(
    #     database="crm_dev"
    # )