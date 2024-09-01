import mysql.connector


def connect_to_mysql():
    config = {
        'user': 'root',
        'password': '12345',
        'host': 'localhost',
        'database': 'database',
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Connected to MySql Database")
        return connection

    except mysql.connector.Error as err:
        print("There is something wrong", err)


def insert_into_table(conn, name, department, position, salary):
    cursor = conn.cursor()

    cursor.execute("""
                insert into employees (name, department, position, salary)
                values (%s, %s, %s, %s)
            """, (name, department, position, salary))

    conn.commit()
    cursor.close()


def read_records(conn):
    cursor = conn.cursor()
    cursor.execute("select * from employees")

    records = cursor.fetchall()
    for row in records:
        print(row)

    cursor.close()


def update_record(conn, new_name, new_dep, new_post, new_salary, employee_id):
    cursor = conn.cursor()
    cursor.execute("""
    update employees set 
            name=%s,
            department=%s,
            position=%s,
            salary=%s
            where id = %s """, (new_name, new_dep, new_post, new_salary, employee_id)
                   )

    conn.commit()
    cursor.close()


def delete_record(conn, employee_id):
    cursor = conn.cursor()

    cursor.execute(
        """
        delete from employees where id=%s
        """, (employee_id,))

    conn.commit()
    cursor.close()



if __name__ == "__main__":
    conn = connect_to_mysql()
    # insert_into_table(conn, "Mahdi", "Marketing", "Coordinator", 3000)
    # insert_into_table(conn, "Adam", "NASA", "Senior Manager", 190000)

    # Read All Records
    print("\nRecords before deletion")
    read_records(conn)

    delete_record(conn, 2)

    print("\nRecords after deletion")

    read_records(conn)


    # update_record(conn, "Ibrahim", "Low", "HR", 3000, 5)
    # print("After updating the records......\n")
    # read_records(conn)


