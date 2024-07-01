# **Payroll Management System**
Welcome to the Payroll Management System! This Python-based system simplifies the management of employee records and payroll tasks.

## **Features**

  - Adding Employee Record: Easily add new employee records to the system.
  - Displaying Records of Employees: View all records of employees currently in the system.
  - Displaying Record of a Particular Employee: Retrieve and display specific details of a particular employee.
  - Deleting Records of All Employees: Remove all employee records from the system.
  - Deleting Record of a Particular Employee: Delete the record of a specific employee.
  - Modification in The Record: Update and modify existing employee records.
  - Displaying Employee Payroll: Access and view payroll information for all employees.
  - Displaying Salary Slip of All Employees: Generate salary slips for all employees.
  - Displaying Salary Slip of a Particular Employee: Generate and view the salary slip for a particular employee.
  - Exit: Option to exit the system.

## **Installation**

To run this system, you need to install the following Python libraries:
Tabulate

### Tabulate is used for displaying data in a tabular format.

```bash 
pip install tabulate 
```

### Mysql.connector :- This library is required to connect Python with MySQL database.

```bash
pip install mysql-connector-python
```

## **Setting Up MySQL Database**

Ensure you have MySQL installed on your system. Create a database named payroll_management and execute the SQL script provided in database_setup.sql to set up the necessary tables.
### Usage
   - Clone this repository to your local machine.
   - Navigate to the directory containing the files.
   - Set your Database Password in DatabasePassword Variable in payroll_management.py 
   - Run python payroll_management.py to start the Payroll Management System.
   - Follow the on-screen instructions to perform various tasks related to employee records and payroll management.

Feel free to explore and customize the system according to your needs!
