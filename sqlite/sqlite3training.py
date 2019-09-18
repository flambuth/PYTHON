#make transaction db

import sqlite3

def make_transaction(customer, amount):
    import datetime
    zeit = datetime.datetime.now()
    time_stamp = f"{customer}-{amount}-{zeit.year}/{zeit.month}/{zeit.day}"
    return time_stamp

conn = sqlite3.connect('transactions.db')

c = conn.cursor()

test_transaction = make_transaction("Simpson", 500)

c.execute("""CREATE TABLE timestamps (
            trans_id integer PRIMARY KEY,
            stamp text NOT NULL
)""")

#c.execute("INSERT INTO timestamps VALUES (?,?)",(1,test_transaction))

c.execute("SELECT * FROM timestamps")
print(c.fetchall())

conn.commit()
conn.close()