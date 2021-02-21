import sqlite3

# Establish connection to local database:
conn = sqlite3.connect('./db.sqlite') # Create database
cur = conn.cursor()

# Print table:
select_test = 'SELECT * from color_combinations_rated'
cur.execute(select_test)
select_test_result = cur.fetchall()
for row in select_test_result:
    print(row)
print(" ")

# Get table info:
table_info = cur.execute("PRAGMA TABLE_INFO({})".format('color_combinations_rated'))
table_info_tuples = [tup[:] for tup in table_info]
print(table_info_tuples)
print(" ")

# Close connection to database:
cur.close()
conn.close()
