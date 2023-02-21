import csv

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)

outfile = open("customer_country2.csv", "w")

outfile.write("FullName,Country\n")

next(csvfile)

for record in csvfile:
    outfile.write(record[1] + " " + record[2] + "," + record[4] + "\n")


outfile.close()
