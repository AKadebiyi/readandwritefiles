import csv

search_name = input("please enter a first name to search: ")

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)

next(csvfile)

foundFlag = False

for rec in csvfile:
    if rec[1].lower() == search_name.lower():
        print("match found")
        print()
        print(f"First Name: {rec[1]}")
        print(f"Last Name: {rec[2]}")
        print(f"City: {rec[3]}")
        print(f"Country: {rec[4]}")
        print(f"Phone: {rec[5]}")
        foundFlag = True

if not foundFlag:
    print("match not found")
