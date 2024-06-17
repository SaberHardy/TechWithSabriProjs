from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("500x400")
root.configure(background='#8fa3c2')

connection_db = sqlite3.connect("/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
cursor_db = connection_db.cursor()


# 5 data types(text, integer, real, null, blob(files))
# cursor_db.execute("""
#         CREATE TABLE IF NOT EXISTS student (
#             first_name TEXT,
#             last_name TEXT,
#             age INTEGER)""")


def save_updates():
    connection_db = sqlite3.connect(
        "/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
    cursor_db = connection_db.cursor()

    record_id_to_update = delete_entry.get()
    cursor_db.execute("""
        UPDATE student SET
        first_name=:first,
        last_name=:last,
        age=:age
        WHERE oid=:oid""",
                      {
                          'first': first_name_update.get(),
                          'last': last_name_update.get(),
                          'age': age_update.get(),
                          'oid': record_id_to_update
                      })

    connection_db.commit()
    connection_db.close()

    top.destroy()


def update_record():
    connection_db = sqlite3.connect(
        "/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
    cursor_db = connection_db.cursor()

    record_to_update = delete_entry.get()
    cursor_db.execute(f"select * from student where oid={record_to_update}")

    # print(f"Record To Update {record_to_update}")
    global top
    top = Toplevel(root)
    top.geometry("500x400")
    top.configure(background='#8fa3c2')

    global first_name_update
    global last_name_update
    global age_update

    first_name_update = Entry(top, width=30)
    first_name_update.grid(row=0, column=1, padx=20)
    Label(top, text="First Name ").grid(row=0, column=0)

    last_name_update = Entry(top, width=30)
    last_name_update.grid(row=1, column=1, padx=20)
    Label(top, text="Last Name ").grid(row=1, column=0)

    age_update = Entry(top, width=30)
    age_update.grid(row=2, column=1, padx=20)
    Label(top, text="Age ").grid(row=2, column=0)

    update_top = Button(top, text="Save Updates", command=save_updates)
    update_top.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

    all_records = cursor_db.fetchall()

    for record in all_records:
        first_name_update.insert(0, record[0])
        last_name_update.insert(0, record[1])
        age_update.insert(0, record[2])

    connection_db.commit()
    connection_db.close()


def add_record():
    connection_db = sqlite3.connect(
        "/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
    cursor_db = connection_db.cursor()

    cursor_db.execute(
        "INSERT INTO student VALUES (:first_name, :last_name, :age)",
        {
            "first_name": first_name_entry.get(),
            "last_name": last_name_entry.get(),
            "age": age_entry.get()
        }
    )
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    age_entry.delete(0, END)

    connection_db.commit()
    connection_db.close()


list_labels = []


def show_records():
    for label in list_labels:
        label.destroy()
    list_labels.clear()

    connection_db = sqlite3.connect(
        "/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
    cursor_db = connection_db.cursor()

    cursor_db.execute("SELECT *, oid FROM student")
    records = cursor_db.fetchall()
    # print(records)

    for record in records:
        label_names = Label(root,
                            text=f"Full name: {record[0] + ' ' + record[1]} has {record[2]} years old \t {record[3]}")
        label_names.grid(column=1, pady=3)
        list_labels.append(label_names)

    connection_db.commit()
    connection_db.close()


def delete_record_func():
    connection_db = sqlite3.connect(
        "/Users/macbook/PycharmProjects/TechWithSabri/Tkinter/Tkinter_databases/school_db.db")
    cursor_db = connection_db.cursor()

    try:
        cursor_db.execute(f"delete from student where oid={str(delete_entry.get())}")
    except:
        print("No inputs")

    delete_entry.delete(0, END)

    connection_db.commit()
    connection_db.close()


first_name_entry = Entry(root, width=30)
first_name_entry.grid(row=0, column=1, padx=20)
Label(root, text="First Name ").grid(row=0, column=0)

last_name_entry = Entry(root, width=30)
last_name_entry.grid(row=1, column=1, padx=20)
Label(root, text="Last Name ").grid(row=1, column=0)

age_entry = Entry(root, width=30)
age_entry.grid(row=2, column=1, padx=20)
Label(root, text="Age ").grid(row=2, column=0)

submit_button = Button(root, text="Add Record to Database", command=add_record)
submit_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

query_records = Button(root, text="Display Records", command=show_records)
query_records.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

delete_entry = Entry(root, width=30)
delete_entry.grid(row=5, column=1)

delete_label = Label(root, text="Id to Update/Delete")
delete_label.grid(row=5, column=0)

delete_button = Button(root, text="Delete", command=delete_record_func)
delete_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

update_button = Button(root, text="Update", command=update_record)
update_button.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

connection_db.commit()
connection_db.close()

root.mainloop()
