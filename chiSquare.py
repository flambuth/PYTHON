import pandas as pd
from env import host,user,password
from scipy import stats


index = ['Male','Female']
columns = ['Republican','Democrat','Independent']

observed = pd.DataFrame(
    [[200,150, 50],[250,300,50]],index=index, columns=columns)

chi2, p, degfree, expected = stats.chi2_contingency(observed)


# Use the data from the employees database to answer these questions:

# Is an employee's gender independent of whether an employee works in sales or marketing? (only look at current employees)
# Is an employee's gender independent of whether or not they are or have been a manager?

def get_db_url(username, hostname, password, database):
    """Returns a string that is formatted correctly to access the database """
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

def make_df_from_db(url, table):
    """Returns a dataframe that is made from one table in a database"""
    return pd.read_sql(f'
    SELECT * FROM {table}
    JOIN dept_emp AS de USING(emp_no)
    JOIN department AS d USING(dep_no)', 
    url)

url = get_db_url(user,host,password,'employees')

emp_df = make_df_from_db(url,'employees')