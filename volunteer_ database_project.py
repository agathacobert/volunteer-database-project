from datetime import date

import sqlite3

# create the database
connection = sqlite3.connect("work_record.db")
cur = connection.cursor()


def create_table():
    # create a table "Volunteer"
    cur.execute(
        """CREATE TABLE IF NOT EXISTS volunteer_data (
        name TEXT,
        finished_at TEXT,
        hours REAL, 
        date_completed DATE)"""
    )

    connection.commit()


def input_data():
    user_input = input(
        "Enter your name, where you finished at, and hours volunteered: "
    )

    name, finished_at, hours = user_input.split(",")

    # strip = remove any excess space user may accid. add
    hours = float(hours.strip())

    date_completed = date.date_completed()

    # insert values into database
    cur.execute(
        """INSERT INTO volunteer_data (name, 
      finished_at, hours, date_completed) VALUES (?,?,?,?)""",
        (name, finished_at, hours, date_completed),
    )
    connection.commit()
    # retrieving and display data

    return name, finished_at, hours, date_completed


def get_data():
    cur.execute("SELECT ROWID, * FROM volunteer_data")
    records = cur.fetchall()

    for index, data in enumerate(records):
        print(index + 1, data)

    return records


def update_data():
    # show the user the data
    data = get_data()
    # ask the user which one they want to update
    row_index = int(input("Which one do you want to update? ")) - 1
    row_data = data[row_index]

    row_id = row_data[0]

    new_data = input("Enter the new values: ")

    name, finished_at, hours = new_data.split(",")

    cur.execute(
        """UPDATE volunteer_data SET name = ?,
      finished_at = ?, hours = ? WHERE ROWID = ?""",
        (name, finished_at, hours, row_id),
    )

    connection.commit()
    print("Data updated successfully!")


def delete_data():
    active = True
    while active is True:
        data = get_data()
        # ask the user which one they want to delete
        row_index = int(input("Which one do you want to delete? ")) - 1
        row_data = data[row_index]

        row_id = row_data[0]

        cur.execute("""DELETE FROM volunteer_data WHERE ROWID = ?""", (row_id,))
        connection.commit()
        print("Data deleted successfully!")

        continue_delete = input("Do you want to delete another? y/n ").lower()
        if continue_delete == "n":
            active = False
    print("Done!")


def run_program():
    action = input(
        "What do you want to do? (input, view, update or delete database?) "
    ).lower()
    if action == "input":
        input_data()
    elif action == "view":
        get_data()
    elif action == "update":
        update_data()
    elif action == "delete":
        delete_data()
    else:
        print("That's not a valid option. Try again!")


run_program()

# END OF FILE
connection.close()
