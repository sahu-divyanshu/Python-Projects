import mysql.connector
import datetime
from tabulate import tabulate
import os
import platform

databasePassword = ""
mydb = mysql.connector.connect(host='localhost', user='root', password=databasePassword, auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Payroll;")
mycursor.execute("USE Payroll;")
query = "CREATE TABLE IF NOT EXISTS Employee(Emp_No INT PRIMARY KEY," \
"Name VARCHAR(50) NOT NULL,Job VARCHAR(20)," \
"Basic_Salary INT,DA FLOAT,HAR FLOAT,Gross_Salary FLOAT," \
"Tax FLOAT, Net_Salary FLOAT);"
mycursor.execute(query)
print("Connected to Payroll Management System Successfully....")


def add_employee():
    try:
        print("Enter Employee Information....")
        emp_no = int(input("Enter Employee Num : "))
        name = input("Enter Employee Name : ")
        job = input("Enter Employee Job : ")
        basic = float(input("Enter Basic Salary : "))
        if job.upper() == "OFFICER":
            da = basic * 0.5
            hra = basic * 0.35
            tax = basic * 0.2
        elif job.upper() == "MANAGER":
            da = basic * 0.45
            hra = basic * 0.30
            tax = basic * 0.15
        else:
            da = basic * 0.40
            hra = basic * 0.25
            tax = basic * 0.1
        gross = basic + da + hra
        net = gross - tax
        rec = (emp_no, name, job, basic, da, hra, gross, tax, net)
        sql = "INSERT INTO Employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        mycursor.execute(sql, rec)
        mydb.commit()
        print("Record Added Successfully......")
    except Exception as e:
        print("Something Went Wrong", e)


def view_all_records():
    try:
        sql = "SELECT * FROM Employee;"
        mycursor.execute(sql)
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("No Record to Display")
        else:
            columns = ['Emp No', 'NAME', 'JOB', 'BASIC SALARY', 'DA', 'HRA', 'GROSS SALARY', 'TAX', 'NET SALARY']
        table = tabulate(my_records, columns, tablefmt="grid")
        print(table)
    except Exception as e:
        print("Something Went Wrong", e)


def view_record():
    try:
        en = int(input("Enter Employee Num : "))
        sql = "SELECT * FROM Employee WHERE Emp_No = %s ;"
        mycursor.execute(sql, (en,))
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("Employee Does Not Exist")
        else:
            print("\n\nRecord of Employee Num : " + str(en))
            columns = ['Emp No', 'NAME', 'JOB', 'BASIC SALARY', 'DA', 'HRA', 'GROSS SALARY', 'TAX', 'NET SALARY']
            table = tabulate(my_records, columns, tablefmt="grid")
            print(table)
    except Exception as e:
        print("Something Went Wrong", e)


def del_all_record():
    try:
        sql = "SELECT * FROM Employee;"
        mycursor.execute(sql)
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("No Record to Delete")
        else:
            ch = input("Do You Want to Delete All the Records(y/n) : ")
        if ch.upper() == 'Y':
            mycursor.execute("DELETE FROM Employee;")
            print("All Records Are Deleted")
            mydb.commit()
    except Exception as e:
        print("Something Went Wrong", e)


def del_record():
    try:
        en = int(input("Enter Employee Num : "))
        sql = "SELECT * FROM Employee WHERE Emp_No = %s ;"
        mycursor.execute(sql, (en,))
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("Employee Does Not Exist")
        else:
            sql = "DELETE FROM Employee WHERE Emp_No = %s;"
            mycursor.execute(sql, (en,))
            print("Record Has Been Deleted")
        mydb.commit()
    except Exception as e:
        print("Something Went Wrong", e)


def modify_record():
    try:
        en = int(input("Enter Employee Num : "))
        sql = "SELECT * FROM Employee WHERE Emp_No = %s;"
        mycursor.execute(sql, (en,))
        my_records = mycursor.fetchone()
        c = mycursor.rowcount
        if c == 0:
            print("Employee Does Not Exist")
        else:
            print("\t\t 1 For Modify Employee's Name")
            print("\t\t 2 For Modify Employee's Job")
            print("\t\t 3 For Modify Employee's Basic Salary")
        choices = int(input("Enter Your Choice : "))
        if choices == 1:
            name = input('Enter Name : ')
            sql = "UPDATE Employee SET Name = %s WHERE Emp_No = %s;"
            mycursor.execute(sql, (name, en,))
            print('Name Modified')
            mydb.commit()
        elif choices == 2:
            job = input('Enter Job : ')
            sql = "UPDATE Employee SET Job = %s WHERE Emp_No = %s;"
            mycursor.execute(sql, (job, en,))
            print('Job Modified')
            mydb.commit()
        elif choices == 3:
            basic = float(input('Enter Basic Salary : '))
            if my_records[2].upper() == "OFFICER":
                da = basic * 0.5
                hra = basic * 0.35
                tax = basic * 0.2
            elif my_records[2].upper() == "MANAGER":
                da = basic * 0.45
                hra = basic * 0.30
                tax = basic * 0.15
            else:
                da = basic * 0.40
                hra = basic * 0.25
                tax = basic * 0.1
            gross = basic + da + hra
            net = gross - tax
            sql = "UPDATE Employee SET Basic_Salary = %s,DA = %s,HAR = %s,Gross_Salary = %s,Tax = %s,Net_Salary = %s WHERE Emp_No = %s;"
            mycursor.execute(sql, (basic, da, hra, gross, tax, net, en))
            print('Salary Modified')
            mydb.commit()
        else:
            print("Invalid Choice")
    except Exception as e:
        print('Something Went Wrong', e)


def display_payroll():
    try:
        sql = "SELECT * FROM Employee"
        mycursor.execute(sql)
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("No Record to Display Payroll")
        else:
            now = datetime.datetime.now()
            print("\n\n\n")
            print("*" * 100)
            print("\t\t\t\t\t\tPayroll")
            print("*" * 100)
            print("Current Date and Time:", end='')
            print(now.strftime("%Y-%m-%d, %H:%M:%S"))
            columns = ['Emp No', 'NAME', 'JOB', 'BASIC SALARY', 'DA', 'HRA', 'GROSS SALARY', 'TAX', 'NET SALARY']
            table = tabulate(my_records, columns, tablefmt="grid")
            print(table)
    except Exception as e:
        print("Something Went Wrong", e)


def display_salary_slips():
    try:
        sql = "SELECT * FROM Employee"
        mycursor.execute(sql)
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("No Record to Display Salary Slip")
        else:
            now = datetime.datetime.now()
            print("\n\n\n")
            print("*" * 100)
            print("\t\t\t\t\t\tSalary Slip")
            print("*" * 100)
            print("Current Date and Time:", end='')
            print(now.strftime("%Y-%m-%d, %H:%M:%S"))
            columns = ['Emp No', 'NAME', 'JOB', 'BASIC SALARY', 'DA', 'HRA', 'GROSS SALARY', 'TAX', 'NET SALARY']
            table = tabulate(my_records, columns, tablefmt="grid")
            print(table)
    except Exception as e:
        print("Something Went Wrong", e)


def display_salary_slip():
    try:
        en = int(input("Enter Employee Number Whose Salary Slip You Want To Retrieve :"))
        sql = "SELECT * FROM Employee WHERE Emp_No = %s ;"
        mycursor.execute(sql, (en,))
        my_records = mycursor.fetchall()
        c = mycursor.rowcount
        if c == 0:
            print("Employee Does Not Exist")
        else:
            now = datetime.datetime.now()
            print("\n\n\n\t\t\t\t\t\tSALARY SLIP")
            print("Current Date and Time:", end='')
            print(now.strftime("%Y-%m-%d, %H:%M:%S"))
            columns = ['Emp No', 'NAME', 'JOB', 'BASIC SALARY', 'DA', 'HRA', 'GROSS SALARY', 'TAX', 'NET SALARY']
            table = tabulate(my_records, columns, tablefmt="grid")
            print(table)
    except Exception as e:
        print("Something Went Wrong", e)


def menu_set():
    print('~' * 130)
    print("\t\t\t\t\tMain Menu") 
    print('~' * 130)
    print("\t\t 1 For Adding Employee Record")
    print("\t\t 2 For Displaying Records of Employees ")
    print("\t\t 3 For Displaying Record of a Particular Employee")
    print("\t\t 4 For Deleting Records of All Employees")
    print("\t\t 5 For Deleting Record of a Particular Employee")
    print("\t\t 6 For Modification in The Record")
    print("\t\t 7 For Displaying Employee Payroll")
    print("\t\t 8 For Displaying Salary Slip of All Employees")
    print("\t\t 9 For Displaying Salary Slip of a Particular Employee")
    print("\t\t 10 For Exit")
    try:
        choice = int(input("\t\tEnter Your Choice : "))
        if choice == 1:
           add_employee()

        elif choice == 2:
           view_all_records()

        elif choice == 3:
           view_record()

        elif choice == 4:
           del_all_record()

        elif choice == 5:
           del_record()

        elif choice == 6:
           modify_record()

        elif choice == 7:
           display_payroll()

        elif choice == 8:
           display_salary_slips()

        elif choice == 9:
           display_salary_slip()

        elif choice == 10:
          exit()

        else:
           print("\t\tEnter Valid Choice")
        
    except ValueError:
        exit("\nHy! That's Not A Number")

def main(run = 'y'):
    while run.lower() == 'y':
        if platform.system() == "Windows":
            os.system('cls')
          
        else:
            os.system('clear')
        menu_set()
         
main()
