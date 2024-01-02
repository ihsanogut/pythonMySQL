import mysql.connector as con

mycon = con.connect(user='root', password='root', host='127.0.0.1', port='3306', database='new_schema')

cursor =mycon.cursor()

query = "SELECT id,name,surname,email FROM new_schema.users;"

cursor.execute(query)

for (id, name, surname, email) in cursor:
    print("id="+str(id)+" name="+str(name)+" surname="+str(surname)+" email="+str(email))

cursor.close()
mycon.close()

