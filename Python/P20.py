"""
In a company an employee is paid as under:
If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the employee'salary is input through the keyboard write a program to find his gross salary.
"""
salary = float(input("Enter the salary: "))
HRA = 500
DA = 0.98 * salary
if salary >= 1500:
    HRA =  0.1 * salary
    DA = 0.9 * salary

gross_salary = salary + HRA + DA
print(gross_salary)