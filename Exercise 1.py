import csv


def main():
    customerfile = open("customers.csv", "r")
    content = csv.reader(customerfile, delimiter=",")

    newfile = open("customer_country.csv", "w")
    acc = 0
    for i in content:
        fullname = i[1] + " " + i[2]
        country = i[4]
        cc_write = csv.writer(
            newfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        cc_write.writerow([fullname, country])
        acc += 1
    cc_write.writerow(["Total number of customers =", acc])
    customerfile.close()
    newfile.close()


main()
