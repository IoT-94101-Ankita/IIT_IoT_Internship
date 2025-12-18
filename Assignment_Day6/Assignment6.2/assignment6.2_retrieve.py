import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_1",
    use_pure=True
)

query = "select * from soil_moisture_"


cursor = connection.cursor()
cursor.execute(query)
soil_moisture_ = cursor.fetchall()
for i in soil_moisture_:
    print(i)
cursor.close()
connection.close()
