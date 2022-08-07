import mysql.connector

print('1')
mydb=mysql.connector.connect(host="web49.lws-hosting.com",database="cp1873034p22_Candid",user = "cp1873034p22_tt",password="L3y.Y[2Zr[PQ",)
print(mydb)

mc = mydb.cursor()
#mc.execute("SHOW DATABASES")
#for db in mc:
#    print(db[0])

mc.execut()
