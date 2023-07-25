import sqlite3

conn = sqlite3.connect('Accounts.db')
c = conn.cursor()

#c.execute("CREATE TABLE USERS ( NAME TEXT, PASSWD TEXT, balance INT, account_no TEXT)")

#c.execute("insert into USERS values('selam', '3452', 160000, '104123'),('eyob','2376', 1265000, '102365'),('lij eyasu','9867', 132000000, '101133'),('silasia','8956', 6542020, '107688')")
#c.execute("insert into USERS values('sam', 'abcd', 20000, '101572')")
#c.execute("insert into USERS values('test1', 'zzzz', 20000, '101572')")

c.execute("select * from USERS ")
result = c.fetchall()

if result == None:
    print("None")
else:
    print("username password balance, acc_no")
    for i in range(len(result)):
        print(result[i])

conn.commit()
conn.close()

