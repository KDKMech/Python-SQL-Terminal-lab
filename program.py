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
    empName = input("what is the name of the employee?")
    empEmployer = input("what is the ID of the company they work for")
    
    cursor.execute("INSERT INTO employees (name, company_id) VALUES (%s, %s)", [empName, empEmployer] )
    connection.commit()




userchoice = 999 



# connection = psycopg2.connect(
#     database="crm_dev"
# )
while int(userchoice) != 9:
    
    userchoice = input(welcome_message)
    match int(userchoice):
        case 1:
            print("one")
            addEmp()
            
            
            
        case 2:
            print("two")
        case 3:
            print("three")
        case 4:
            print("four")
        case 5:
            print("five")
        case 6:
            print("six")
        case 7:
            print("seven")
        case 8:
            print("eight")
        case 9:
            print("Exiting...") 
            connection.close()
            









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