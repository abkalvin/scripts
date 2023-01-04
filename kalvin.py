import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""


)

mycursor = mydb.cursor()
mycursor.execute("show databases")

for x in mycursor:
  print(x)


# mycursor.execute("Create database mohan")
# print("database created successfully")
#
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# print("table created successfully")


# mycursor.execute("INSERT INTO customers (name, address) VALUES ('sona', 'madurai')")
# # val = ("John", "Highway 21")
# # mycursor.execute(sql, val)
#
# mydb.commit()

# name = input("ENTER THE NAME :")
# address = input("ENTER THE ADDRESS:")
# mycursor = mydb.cursor()
#
# sql = ("INSERT INTO customers (name, address) VALUES (%s, %s)")
#
# val = (name, address)
# mycursor.execute(sql, val)
#
# mydb.commit()












