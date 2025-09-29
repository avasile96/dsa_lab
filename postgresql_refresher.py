import psycopg2

conn = psycopg2.connect(host="localhost", 
                        dbname="postgres",
                        user="postgres",
                        password="656463",
                        port="5432")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
            (1, 'Mike', 30, 'm'),
            (2, 'Misa', 12, 'f'),
            (3, 'Al', 32, 'm')
""")

cur.execute("""SELECT * FROM person WHERE name = 'Al';""")

print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age <20""")

for row in cur.fetchall():
    print(row)

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("M", 20))

print(sql)

cur.execute(sql)

print(cur.fetchall())

conn.commit()
cur.close
conn.close()