# Inserting Record 

import pymysql
try:
    connection= pymysql.connect(host="localhost",user="root",passwd="77187718",db="student")
    cursors= connection.cursor()
    # cursors.execute("insert into student values()")
    
except:
    print("Error In Query Please Check It...!")

else:
    print("Record succesfully Added")
    connection.commit()

finally:
    cursors.close()