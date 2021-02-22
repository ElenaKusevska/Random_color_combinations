import sqlite3
import datetime

# Establish connection to local database:
conn = sqlite3.connect('./db.sqlite') # Create database
cur = conn.cursor()

# Create table:
cur.execute('DROP TABLE IF EXISTS color_combinations_rated')
create_table = ( 'CREATE TABLE color_combinations_rated (' 
        + 'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
        + 'time TIME NOT NULL,'
        + 'date DATE NOT NULL,'
        + 'background_col VARCHAR NOT NULL,'
        + 'text_col VARCHAR NOT NULL,'
        + 'rating INTEGER NOT NULL );' )
cur.execute(create_table)

# Create an entry to test the table and database are working:
current_date_time = str(datetime.datetime.now()).split('.')[0]
current_date = current_date_time.split(' ')[0]
current_time = current_date_time.split(' ')[1]
insert_test_value = ( 'INSERT INTO color_combinations_rated (time, date, background_col, text_col, rating) '
     + 'VALUES ( "' + current_time + '", "' + current_date + '", "#ffffff", "#000000", 5);' )
cur.execute(insert_test_value)

# Create another entry to test the table and database are working:
current_date_time = str(datetime.datetime.now()).split('.')[0]
current_date = current_date_time.split(' ')[0]
current_time = current_date_time.split(' ')[1]
insert_test_value = ( 'INSERT INTO color_combinations_rated (time, date, background_col, text_col, rating) '
     + 'VALUES ( "' + current_time + '", "' + current_date + '", "#000000", "#ffffff", 5);' )
cur.execute(insert_test_value)

# Print table:
select_test = ( 'SELECT * from color_combinations_rated' )
cur.execute(select_test)
print(cur.fetchall())

# Get table info:
table_info = cur.execute("PRAGMA TABLE_INFO({})".format('color_combinations_rated'))
table_info_tuples = [tup[:] for tup in table_info]
print(table_info_tuples)
print(" ")

# Commit and close
conn.commit()
cur.close()
conn.close()
