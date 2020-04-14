import pymysql

conn = pymysql.connect(host='ip-172-31-38-19.us-east-2.compute.internal', port=3306, user='root', passwd='passw0rd', db='mysql')

cur = conn.cursor()
cur.execute("SELECT * FROM users")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()
