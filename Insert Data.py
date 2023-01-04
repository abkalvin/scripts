import csv
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabse"
)
with open("C:/Users/hp/Desktop/DUMP.xlsx") as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    print(csvfile)

    all_value = []
    for row in csvfile:
        # print(row[0])

        value = (row[0], row[1], row[2], row[3], row[4], row[5])
        all_value.append(value)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE CAR_DATA (Car_Name VARCHAR(20), Year int, Selling_Price, Data_Speed FLOAT, Signal_strength INT,LSA VARCHAR(20))")
query = "insert into `car_data` (Service_Provider, Technology, Test_type, Data_Speed, Signal_strength,LSA) values(%s, %s, %s, %s, %s, %s)"

mycursor.executemany(query, all_value)
mydb.commit()
print("Inserted successfully")

