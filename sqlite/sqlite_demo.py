import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employee (
#             first text,
#             last text,
#             pay integer
# )""")

#c.execute("""INSERT INTO employee VALUES ('Bill','Dautervie',50000)""")
c.execute("SELECT * FROM employee WHERE last='Dautervie'")

print(c.fetchone())

conn.commit()
conn.close()