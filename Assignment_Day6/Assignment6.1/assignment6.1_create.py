import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

id=int(input("Enter ID:"))
temp=int(input("Enter temperature:"))
humidity=float(input("Enter humidity:"))
timestamp=input("Enter Timestamp:")

query= f"insert into sensor_readings values({id},{temp},{humidity},'{timestamp}');"


cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()