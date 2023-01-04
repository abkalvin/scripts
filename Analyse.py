import csv
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Data_Analyst"
)
with open("C:\\Users\hp\Downloads\Copy of Data For Evaluation - Problem_2.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    # print(type(csvfile))

    all_value = []
    for row in csvfile:

        # print(row[0])

        value = (row[0], row[1])
        all_value.append(value)
    # print(all_value.pop(0))

    print(all_value.pop(2))
    # print(all_value[0])

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE Data (date_time varchar(255), instance_id varchar(255))")
# query = "insert into `Data` (date_time, instance_id) values(%s, %s)"
#
# mycursor.executemany(query, all_value)
# mydb.commit()
# print("Inserted successfully")
