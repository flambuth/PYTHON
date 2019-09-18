#Converted my list of dictionaries stashed inside customers.json
#into a database with two tables.
#Customers table has been transfereed. Working on making a transactions table.
import json, sqlite3

# json_file = "customers.json"

#customers list is a list of dictionaries
with open('/Users/fredricklambuth/Documents/Notes/PYTHON/checkbook_deluxe/customers.json', 'r') as f: 
    customers_list = json.load(f)

conn = sqlite3.connect('customers.db')

c = conn.cursor()

# Makes a blank table for cusomter name and balance
# c.execute("""CREATE TABLE transaction ( 
#     id integer PRIMARY KEY, 
#     user text NOT NULL,
#     amount integer)""")    

#I don't know why this works and the other two dont.
c.execute("""CREATE TABLE customers (
            username text PRIMARY KEY,
            balance integer
            )""")                                                                                                                  
# Makes a transaction table. Finish up later
# c.execute("""CREATE TABLE timestamps ( 
#     name text PRIMARY KEY, 
#     balance integer NOT NULL)""")


#The JSON was dumped into customer_list, which I iterated through and inserted each as a row
#in the customers table the customers database
for i in customers_list: 
    c.execute("INSERT INTO customers VALUES (?,?)",(i['name'],i['balance'])) 

#Verify the rows are in the table
c.execute("SELECT * FROM customers")
print(c.fetchall())   

#Uncomment if you wanna make some changes. This is for documentation.
conn.commit()
conn.close()