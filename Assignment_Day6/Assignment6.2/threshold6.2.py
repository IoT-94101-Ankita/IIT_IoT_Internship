import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_1",
    use_pure=True
)

threshold = float(input("Enter moisture level threshold: "))

query = f"select * from soil_moisture_ where moisture_level < {threshold};"

# create cursor to execute query
cursor = connection.cursor()

# execute query with cursor
cursor.execute(query)

# get required data from cursor
soil_moisture_ = cursor.fetchall()

# print data
for i in soil_moisture_:
    print(i)

# close the cursor
cursor.close()

# close connection with mysql server
connection.close()
