import csv


salesfile = open("sales.csv", "r")
sales = csv.reader(salesfile, delimiter=",")
next(sales)

newfile = open("salesreport.csv", "w")
sales_write = csv.writer(newfile)
sales_write.writerow(["Customer", "Total"])


totalsales = {}

for i in sales:
    ID = i[0]
    sales = float(i[3]) + float(i[4]) + float(i[5])
    if ID in totalsales:
        totalsales[ID] += sales
    else:
        totalsales[ID] = sales

for key, value in totalsales.items():
    value = round(value, 2)
    sales_write.writerow([key, value])

salesfile.close()
newfile.close()
