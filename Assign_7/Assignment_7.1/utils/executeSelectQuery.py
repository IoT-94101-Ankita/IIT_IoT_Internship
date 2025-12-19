from utils.dbConnection import getBDConnection

# To execute SELECT query

def executeSelectQuery(query):
    connection = getBDConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data