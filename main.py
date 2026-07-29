
import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
course TEXT,
marks REAL
)
""")
conn.commit()


def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students VALUES(?,?,?,?,?)",
        (id, name, age, course, marks)
    )
    conn.commit()
    print("Student Added Successfully")


def view_students():
    df = pd.read_sql_query("SELECT * FROM students", conn)
    print(df)


def search_student():
    sid = int(input("Enter Student ID: "))
    df = pd.read_sql_query(
        f"SELECT * FROM students WHERE id={sid}", conn
    )
    print(df)


def update_marks():
    sid = int(input("Student ID: "))
    marks = float(input("New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (marks, sid)
    )
    conn.commit()
    print("Updated Successfully")


def delete_student():
    sid = int(input("Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )
    conn.commit()
    print("Deleted Successfully")


def statistics():
    df = pd.read_sql_query("SELECT * FROM students", conn)

    print("\nAverage Marks:", df["marks"].mean())

    topper = df.loc[df["marks"].idxmax()]
    print("\nTopper")
    print(topper)


while True:

    print("""
1 Add Student
2 View Students
3 Search Student
4 Update Marks
5 Delete Student
6 Statistics
7 Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        statistics()

    elif choice == "7":
        break

    else:
        print("Invalid Choice")

conn.close()