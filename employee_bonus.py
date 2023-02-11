import csv


employeefile = open("EmployeePay.csv", "r")
employee = csv.reader(employeefile, delimiter=",")

next(employee)

for i in employee:
    bonus = float(i[4]) * float(i[3])
    totalpay = float(i[3]) + bonus
    print("Employee ID:", i[0])
    print("First Name:", i[1])
    print("Last Name:", i[2])
    print("Total Pay:", totalpay)
    print()

employee.close()
