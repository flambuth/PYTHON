import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

emp_1 = Employee('Jon','Arbuckle', 88000)
emp_1 = Employee('Susie','Derkins',99000)
print(emp_1.first, emp_1.last)

# c.execute("""CREATE TABLE employee (
#             first text,
#             last text,
#             pay integer
# )""")

#c.execute("DELETE FROM employee WHERE first='LouAnne'")
#c.execute("INSERT INTO employee VALUES ('LouAnne','Platter',55000)")
#The secure way to pass stuff to SQlite commands
#c.execute("INSERT INTO employee VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))

c.execute("SELECT * FROM employee")

print(c.fetchall())

conn.commit()
conn.close()