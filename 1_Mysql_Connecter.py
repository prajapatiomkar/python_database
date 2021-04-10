import pymysql

try:
    connection = pymysql.connect(host="localhost",user="root",passwd="77187718",db="student")
    cursors=connection.cursor()
    # print(cursors)           #To Check Connection Is Established Or Not
except:
    print("Error In DB Operation")
else:
    cursors.close()