import sqlite3

conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
        VALUES (1,'Andrew','Allan',21,30000.00,'manager')");

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
        VALUES (2,'Tito','Tish',25,50000.00,'salesman')");

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
        VALUES (3,'kid','boy',22,25000.00,'Trainer')");
conn.commit()
print("Successfully inserted values in Company1 table")

conn.close()
