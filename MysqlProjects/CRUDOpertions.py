import mysql.connector


def create_table():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='database'
        )
        cursor = conn.cursor()

        create_table_query = """
            create table if not exists employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                department VARCHAR(255),
                position VARCHAR(255),
                salary FLOAT
            )
        """

        cursor.execute(create_table_query)
        print("The table has been created successfully!")

    except mysql.connector.Error as err:
        print("There is something wrong", err)

    finally:
        cursor.close()
        conn.close()


create_table()










